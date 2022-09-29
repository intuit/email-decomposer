
import os
import pandas as pd

curr_path = os.path.dirname(os.path.realpath(__file__)) if '__file__' in globals() else os.getcwd()
emails_mock = pd.read_csv(curr_path + '/mocks/emails.csv', skip_blank_lines=False)['email']
first_names_mock = pd.read_csv(curr_path + '/mocks/first_names.csv', skip_blank_lines=False)['first_name']
last_names_mock = pd.read_csv(curr_path + '/mocks/last_names.csv', skip_blank_lines=False)['last_name']
