import unittest

from parsers import IbmParser

class TestIbmParserDataSciencePage(unittest.TestCase):
    '''Test IBM Parser against one data science job page'''

    def setUp(self):
        '''Get the file contents'''
        with open('tests/ibm_data_science.html') as file_obj:
            self.PAGE_CONTENT = file_obj.read()

    def test_title_extraction(self):
        '''Test successful extraction of the title'''
        expected_title = 'Data Engineer (Datastage)'
        parser = IbmParser(self.PAGE_CONTENT)
        self.assertEqual(parser.get_job_metadata()['title'], expected_title)

    def test_introduction_extraction(self):
        '''Test successful extraction of the introduction content'''
        expected_intro = 'As a Data Engineer at IBM, you will help transform our clients’ data into tangible business value by analyzing information, communicating outcomes and collaborating on product development. Work with Best in Class open source and visual tools, along with the most flexible and scalable deployment options. Whether it’s investigating patient trends or weather patterns, you will work to solve real world problems for the industries transforming how we live.'
        self.maxDiff = None
        parser = IbmParser(self.PAGE_CONTENT)
        job_m = parser.get_job_metadata()
        self.assertMultiLineEqual(parser.get_job_metadata()['introduction'], expected_intro)


    def test_roles_responsibilities_extraction(self):
        '''Test successful extraction of the roles and responsibilities content'''
        parser = IbmParser(self.PAGE_CONTENT)
        extracted_content = parser.get_job_metadata()['roles_and_responsibilities']
        expected_content = "At IBM, work is more than a job - it's a calling: To build. To design. To code. To consult. To think along with clients and sell. To make markets. To invent. To collaborate. Not just to do something better, but to attempt things you've never thought possible. Are you ready to lead in this new era of technology and solve some of the world's most challenging problems? If so, let’s talk."
        self.assertIn(expected_content, extracted_content)
        expected_content = "Responsibilities include:\nCommunicate work to and receive feedback by technical and non-technical "
        self.assertIn(expected_content, extracted_content)
        expected_last_item = "CIODEM20"
        self.assertIn(expected_last_item, extracted_content)

    def test_required_skills_and_qualification(self):
        '''Test successful extraction of required skills and qualifications.'''
        parser = IbmParser(self.PAGE_CONTENT)
        required_stuff = parser.get_job_metadata()['required_stuff']
        expected_first_requirement = "5+ years of experience as data professional (big data solutions)"
        expected_last_requirement = "Proven understanding and proficiency of database administration and data structures"
        self.assertIn(expected_first_requirement, required_stuff)
        self.assertIn(expected_last_requirement, required_stuff)

    def test_preferred_skills_and_qualification(self):
        '''Test successful extraction of preferred skills and qualifications.'''
        parser = IbmParser(self.PAGE_CONTENT)
        preferred_stuff = parser.get_job_metadata()['preferred_stuff']
        expected_first_preferrence = "Significant concentration in a quantitative field"
        expected_last_preferrence = "Experience with Agile/Scrum methodologies/development – ability to accurately size user stories"
        self.assertIn(expected_first_preferrence, preferred_stuff)
        self.assertIn(expected_last_preferrence, preferred_stuff)
