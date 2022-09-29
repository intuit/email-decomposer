from .mocks_generator import *


def test_generate_mocks():
    first_names_mock, last_names_mock, emails_mock = generate_mocks(10)
    assert len(first_names_mock) == 10
    assert len(last_names_mock) == 10
    assert len(emails_mock) == 10