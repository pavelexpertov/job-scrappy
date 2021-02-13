import unittest

from parsers import BloombergParser

class TestBloombergParserWithAiGroupEngineer(unittest.TestCase):
    '''Test bloomberg parser for a job of AI group software engineer'''

    @classmethod
    def setUpClass(cls):
        '''Get the html content'''
        with open('tests/bloomberg_ai_group_software_engineer.html') as file_obj:
            cls.HTML_CONTENT = file_obj.read()

    def test_more_about_us_extraction(self):
        '''Test extraction of 'More about us:' sub-header'''
        parser = BloombergParser(self.HTML_CONTENT)
        roles_and_responsibilities_content = parser.get_job_metadata()['roles_and_responsibilities']
        expected_line_1 = "The AI Group is the central engineering group with over 150 researchers"
        self.assertIn(expected_line_1, roles_and_responsibilities_content)
        expected_line_2 = "Parallel and distributed systems"
        self.assertIn(expected_line_2, roles_and_responsibilities_content)


    def test_for_none_when_extracting_preferred_requirments(self):
        '''Test for None when extracting preferred stuff'''
        parser = BloombergParser(self.HTML_CONTENT)
        preferred_stuff = parser.get_job_metadata()['preferred_stuff']
        self.assertEqual('', preferred_stuff)


class TestBloombergParserWithMlEngineerDataAutomation(unittest.TestCase):
    '''Test bloomberg parser for a job of Machine Learning engineer - data automation'''

    @classmethod
    def setUpClass(cls):
        '''Get the html content'''
        with open('tests/bloomberg_ml_engineer_data_automation.html') as file_obj:
            cls.HTML_CONTENT = file_obj.read()

    def test_for_in_the_upcoming_year_without_more_about_us_extraction(self):
        '''Test for successful extraction of 'in the upcoming year' when 'more about us' is missing'''
        parser = BloombergParser(self.HTML_CONTENT)
        roles_and_responsibilities = parser.get_job_metadata()['roles_and_responsibilities']
        self.assertIn('Replace our traditional annotation models with modern', roles_and_responsibilities)
        not_expected_intro_content = "On the Data Automation team, we develop machine learning models and"
        self.assertNotIn(not_expected_intro_content, roles_and_responsibilities)

    def test_for_we_would_love_to_see_extraction(self):
        '''Test for successful extraction for preferred_stuff'''
        parser = BloombergParser(self.HTML_CONTENT)
        preferred_stuff = parser.get_job_metadata()['preferred_stuff']
        expected_line = "Knowledge of advanced concepts such as weakly supervised learning, reinforcement learning and active learning"
        self.assertIn(expected_line, preferred_stuff)
        not_expected_line = "A strong statistical background in ML, NLP, deep learning models along with familiarity"
        self.assertNotIn(not_expected_line, preferred_stuff)
