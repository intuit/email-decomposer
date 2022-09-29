
import names
import pandas as pd
import random
import os
import sys

curr_path = os.path.dirname(os.path.realpath(__file__)) if '__file__' in globals() else os.getcwd()


def mock_first_names(n: int=10000):
    first_names = []
    for i in range(n):
        first_names.append(names.get_first_name())
    return pd.Series(first_names).str.lower().rename('first_name')


def mock_last_names(n: int=10000):
    last_names = []
    for i in range(n):
        last_names.append(names.get_last_name())
    return pd.Series(last_names).str.lower().rename('last_name')


def mock_emails(first_names_mock, last_names_mock, n: int=10000):
    patterns = ['{first_name}_{last_name}@domain.com',
                '{last_name}_{first_name}@domain.com',
                '{first_name}{last_name}@domain.com',
                '{last_name}{first_name}@domain.com',
                '{first_name}a@domain.com',
                'a{last_name}@domain.com']
    emails = []
    for i in range(n):
        pattern = random.choice(patterns)
        emails.append(pattern.format(first_name=first_names_mock.loc[i], last_name=last_names_mock.loc[i],))
    return pd.Series(emails).str.lower().rename('email')


def generate_mocks(n=10000):
    first_names_mock = mock_first_names(n)
    last_names_mock = mock_last_names(n)
    emails_mock = mock_emails(first_names_mock, last_names_mock, n)
    return first_names_mock, last_names_mock, emails_mock


if "pytest" not in sys.modules:
    first_names_mock, last_names_mock, emails_mock = generate_mocks()
    first_names_mock.to_csv('mocks/first_names.csv', index=False)
    last_names_mock.to_csv('mocks/last_names.csv', index=False)
    emails_mock.to_csv('mocks/emails.csv', index=False)