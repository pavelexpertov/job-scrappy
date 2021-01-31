import unittest

from parsers import FacebookParser

class TestFacebookResearchScientistLangaugeRole(unittest.TestCase):
    '''Test Facebook Career parsers for a research scientist langauge role'''

    def setUp(self):
        '''Get html content'''
        with open('tests/facebook_research_scientist_langauge_role.html') as file_obj:
            self.HTML_CONTENT = file_obj.read()

    def test_title_extraction(self):
        '''Test for successful extraction of a title.'''
        breakpoint()
        parser = FacebookParser(self.HTML_CONTENT)
        title = parser.get_job_metadata()['title']
        self.assertEqual('Research Scientist, Language', title)

    def test_overview_extraction(self):
        '''Test for successful extraction for introduction_content'''
        pass

    def test_roles_and_responsibilities_extraction(self):
        '''Test for successful extraction for roles and responsibilities'''
        pass

    def test_required_stuff_extraction(self):
        '''Test for successful extraction for required_stuff'''
        pass

    def test_preferred_stuff_extraction(self):
        '''Test for successful extraction for preferred_stuff'''
        pass
