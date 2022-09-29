import pandas as pd
import numpy as np

from email_decomposer.EmailDecomposer import EmailDecomposer

email_decomposer = EmailDecomposer()


class TestEmailDecomposer:

    def test_fuzzily_get_email_full_name(self):
        result = email_decomposer.decompose('sarahk42@gmail.com')
        assert result['first_name'] == 'Sarah'
        result = email_decomposer.decompose('moshe.cohen@gmail.com')
        assert result['first_name'] == 'Moshe' and result['last_name'] == 'Cohen'
        result = email_decomposer.decompose('cohen.moshe@gmail.com')
        assert result['first_name'] == 'Moshe' and result['last_name'] == 'Cohen'
        result = email_decomposer.decompose('cohenmoshe@gmail.com')
        assert result['first_name'] == 'Moshe' and result['last_name'] == 'Cohen'
        result = email_decomposer.decompose('moshe@gmail.com')
        assert result['first_name'] == 'Moshe'
        result = email_decomposer.decompose('cohen@gmail.com')
        assert result['last_name'] == 'Cohen'
        result = email_decomposer.decompose('mcohen@gmail.com')
        assert result['last_name'] == 'Cohen'
        result = email_decomposer.decompose('rbrownlr@gmail.com')
        assert result['first_name'] == ''
        result = email_decomposer.decompose('ray_smith@gmail.com')
        assert result['first_name'] == 'Ray'
        result = email_decomposer.decompose('rbrownlr@gmail.com')
        assert result['last_name'] == ''
        result = email_decomposer.decompose('rbrownlr@gmail.com', True)
        assert result['last_name'] == '' and result['host'] == 'gmail.com'

    def test_fuzzily_get_emails_full_names(self):
        result = email_decomposer.decompose(['sarahk42@gmail.com'])
        assert result.iloc[0]['first_name'] == 'Sarah'
        result = email_decomposer.decompose(['sarahk42@gmail.com'], True)
        assert result.iloc[0]['first_name'] == 'Sarah' and result.iloc[0]['host'] == 'gmail.com'

    def test_decompose(self):
        email_data = email_decomposer.decompose(['johndue@intuit.com'])
        assert len(email_data) > 0

    def test_index(self):
        emails = pd.Series(index=[0, 2], data=['stevensmith@intuit.com', 'johndue@intuit.com'])
        email_data = email_decomposer.decompose(emails)
        assert np.all(email_data.index == emails.index)
