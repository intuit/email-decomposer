import re
from typing import Sequence

import pandas as pd
from email_decomposer.FullName import FullName

import nltk
import os

nltk.download('words')
nltk.download('wordnet')
lemmatizer = nltk.stem.WordNetLemmatizer()

curr_path = os.path.dirname(os.path.realpath(__file__)) if '__file__' in globals() else os.getcwd()

all_first_names_set = set(pd.read_csv(curr_path + '/resources/dist.male.first.txt', sep=r'\s+', header=None)[0].dropna().str.lower().values) | set(pd.read_csv(curr_path + '/resources/dist.female.first.txt', sep=r'\s+', header=None)[0].dropna().str.lower().values)
all_last_names_set = set(pd.read_csv(curr_path + '/resources/Names_2010Census.txt', sep=',')['name'].dropna().str.lower().values)


class EmailDecomposer:

    def __init__(self) -> None:
        self.emails_full_names_functions = [self.__get_email_full_name_using_sep,
                                            self.__get_email_first_name_perfect_match,
                                            self.__get_email_last_name_perfect_match,
                                            self.__get_email_full_name_perfect_match,
                                            self.__get_email_full_name_perfect_match_reversed,
                                            self.__get_email_last_name_near_perfect_match,
                                            self.__get_email_first_name_near_perfect_match]
        # self.__get_email_first_name_where_last_name_not_found,
        # self.__get_email_last_name_where_first_name_not_found]
        self.words_set = set(nltk.corpus.words.words())

    def fuzzily_get_email_full_name(self, email: str) -> FullName:
        email = email.lower()
        email_prefix = email.split(sep='@', maxsplit=1)[0]
        cleaned = re.sub(r'(?:^[\d]+)|(?:[+.\-_\d]+$)', '', email_prefix)
        lemma = lemmatizer.lemmatize(cleaned)
        if lemma in self.words_set:
            return FullName('', '')
        for func in self.emails_full_names_functions:
            full_name = func(cleaned)
            if full_name is not None and not full_name.is_empty():
                return full_name
        return FullName('', '')

    def __to_series(self, data: Sequence[object], name: str, dtype: object) -> pd.Series:
        if type(data) == pd.Series:
            return data
        return None if data is None else pd.Series(data).reset_index(drop=True).rename(name).astype(dtype)

    def fuzzily_get_emails_full_names(self, emails: Sequence[str]) -> pd.DataFrame:
        emails = self.__to_series(emails, 'email', str)
        emails = emails.str.lower()
        return emails.apply(lambda email: self.fuzzily_get_email_full_name(email).to_series())

    def decompose(self, data: object, get_host=False) -> object:
        if isinstance(data, str):
            return self.str_decompose(data, get_host)
        elif isinstance(data, Sequence) or isinstance(data, pd.Series):
            return self.seq_decompose(data, get_host)
        else:
            return None

    def str_decompose(self, email: str, get_host=False) -> dict:
        result = self.fuzzily_get_email_full_name(email.lower()).to_dict()
        if get_host:
            host = email.split(sep='@', maxsplit=2)[1]
            result['host'] = host
        return result

    def seq_decompose(self, emails: Sequence[str], get_host=False) -> pd.DataFrame:
        original_index = None
        if type(emails) == pd.Series:
            original_index = emails.index
        else:
            emails = pd.Series(emails)
        full_names = self.fuzzily_get_emails_full_names(emails)
        if get_host:
            hosts = emails.str.split(pat='@', n=2, expand=True)[1].rename('host')
            return full_names.join(hosts.to_frame()).set_index(original_index if original_index is not None else emails)
        else:
            return full_names.set_index(original_index if original_index is not None else emails)

    def __get_email_full_name_using_sep(self, prefix: str) -> FullName:
        first_name = ''
        last_name = ''
        split = re.split(r'[+.\-_\d]+', prefix)
        if len(split) > 1:
            first_name_candidate = re.sub(r'(?:^[\d]+)|(?:[\d]+$)', '', split[0])
            if first_name_candidate in all_first_names_set:
                first_name = first_name_candidate
            last_name_candidate = re.sub(r'(?:^[\d]+)|(?:[\d]+$)', '', split[-1])
            if last_name_candidate in all_last_names_set:
                last_name = last_name_candidate
            full_name = FullName(first_name, last_name)
            if not full_name.is_full():
                full_name_reversed = self.__get_email_full_name_using_sep_reversed(prefix)
                if full_name_reversed.is_full():
                    return full_name_reversed
                else:
                    return full_name
        return FullName(first_name, last_name)

    def __get_email_full_name_using_sep_reversed(self, prefix: str) -> FullName:
        first_name = ''
        last_name = ''
        split = re.split(r'[+.\-_\d]+', prefix)
        if len(split) > 1:
            first_name_candidate = re.sub(r'(?:^[\d]+)|(?:[\d]+$)', '', split[1])
            if first_name_candidate in all_first_names_set:
                first_name = first_name_candidate
            last_name_candidate = re.sub(r'(?:^[\d]+)|(?:[\d]+$)', '', split[0])
            if last_name_candidate in all_last_names_set:
                last_name = last_name_candidate
        return FullName(first_name, last_name)

    def __get_email_full_name_perfect_match(self, prefix: str) -> FullName:
        first_name = ''
        last_name = ''
        for i in range(len(prefix) - 3, 2, -1):
            if prefix[:i] in all_first_names_set and prefix[i:] in all_last_names_set:
                first_name = prefix[:i]
                last_name = prefix[i:]
                break
        return FullName(first_name, last_name)

    def __get_email_full_name_perfect_match_reversed(self, prefix: str) -> FullName:
        first_name = ''
        last_name = ''
        for i in range(len(prefix) - 3, 2, -1):
            if prefix[:i] in all_last_names_set and prefix[i:] in all_first_names_set:
                first_name = prefix[i:]
                last_name = prefix[:i]
                break
        return FullName(first_name, last_name)

    def __get_email_first_name_perfect_match(self, prefix: str) -> FullName:
        first_name = ''
        last_name = ''
        if prefix in all_first_names_set:
            first_name = prefix
        return FullName(first_name, last_name)

    def __get_email_last_name_perfect_match(self, prefix: str) -> FullName:
        first_name = ''
        last_name = ''
        if prefix in all_last_names_set:
            last_name = prefix
        return FullName(first_name, last_name)

    def __get_email_last_name_near_perfect_match(self, prefix: str) -> FullName:
        first_name = ''
        last_name = ''
        candidate = '' if len(prefix) < 4 else prefix[1:]
        if candidate in all_last_names_set:
            last_name = candidate
        return FullName(first_name, last_name)

    def __get_email_first_name_near_perfect_match(self, prefix: str) -> FullName:
        first_name = ''
        last_name = ''
        candidate = '' if len(prefix) < 4 else prefix[:-1]
        if candidate in all_first_names_set:
            first_name = candidate
        return FullName(first_name, last_name)
