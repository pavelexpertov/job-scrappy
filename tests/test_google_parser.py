import json
import unittest

from parsers import GoogleParser

class TestGoogleJobParser(unittest.TestCase):
    '''Test Google Job parser'''

    def setUp(self):
        '''Get json metadata'''
        with open('tests/google_job_json_metadata.json') as file_obj:
            self.JSON_DATA = json.loads(file_obj.read())

    def test_successful_title_extraction(self):
        '''Test successful extraction of title'''
        parser = GoogleParser(self.JSON_DATA)
        metadata = parser.get_job_metadata()
        self.assertEqual('Senior Data Scientist, Waze', metadata['title'])
