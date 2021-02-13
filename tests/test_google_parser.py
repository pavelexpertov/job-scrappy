import json
import unittest

from parsers import GoogleParser

class TestGoogleJobParser(unittest.TestCase):
    '''Test Google Job parser'''

    def setUp(self):
        '''Get json metadata'''
        with open('tests/google_senior_data_scientist_waze_role.json') as file_obj:
            self.JSON_DATA = json.loads(file_obj.read())

    def test_title_extraction(self):
        '''Test extracted value of 'title'''
        parser = GoogleParser(self.JSON_DATA)
        metadata = parser.get_job_metadata()
        self.assertEqual('Senior Data Scientist, Waze', metadata['title'])

    def test_introduction_extraction(self):
        '''Test extracted value of 'introduction'''
        parser = GoogleParser(self.JSON_DATA)
        metadata = parser.get_job_metadata()
        expected_start = "At Google, data drives all of our decision-making. Quantitative Analysts work all across the organization to help shape Google's business and technical strategies by processing, analyzing and interpreting huge data sets."
        message = "First sentence doesn't match with the returned metadata for 'introduction'."
        self.assertTrue(metadata['introduction'].startswith(expected_start), msg = message)
        expected_end = "From Google Ads to Chrome, Android to YouTube, Social to Local, Google engineers are changing the world one technological achievement after another."
        message = "Last sentence doesn't match with the returned metadata for 'introduction'."
        self.assertTrue(metadata['introduction'].endswith(expected_end), msg = message)

    def test_roles_and_responsibilities_extraction(self):
        '''Test extracted value of 'roles_and_responsibilities'''
        parser = GoogleParser(self.JSON_DATA)
        metadata = parser.get_job_metadata()
        content = metadata['roles_and_responsibilities']
        expected_start = "- Work with large, complex data sets."
        message = "First sentence doesn't match with the returned metadata for 'roles_and_responsibilities'."
        self.assertTrue(content.startswith(expected_start), msg=message)
        expected_end = "Work closely with Engineers and Product teams to identify opportunities for, design, and assess improvements of Google products."
        message = "Last sentence doesn't match with the returned metadata for 'roles_and_responsibilities'."
        self.assertTrue(content.endswith(expected_end), msg=message)
