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
        parser = FacebookParser(self.HTML_CONTENT)
        title = parser.get_job_metadata()['title']
        self.assertEqual('Research Scientist, Language', title)

    def test_overview_extraction(self):
        '''Test for successful extraction for introduction_content'''
        parser = FacebookParser(self.HTML_CONTENT)
        introduction_content = parser.get_job_metadata()['introduction']
        expected_start = "Facebook is seeking a Research Scientist to join our AI Research Team, a research organization focused on making significant progress in AI."
        self.assertTrue(introduction_content.startswith(expected_start), msg="First sentence of introduction content doesn't match.")
        expected_end = "The ideal candidate will have a keen interest in producing new science to understand intelligence and technology to make computers more intelligent."
        self.assertTrue(introduction_content.endswith(expected_end), msg="Last sentence of introduction content doesn't match.")

    def test_roles_and_responsibilities_extraction(self):
        '''Test for successful extraction for roles and responsibilities'''
        parser = FacebookParser(self.HTML_CONTENT)
        responsibilities = parser.get_job_metadata()['roles_and_responsibilities']
        expected_first_point = "- Lead research to advance the science and technology of intelligent machines"
        self.assertTrue(responsibilities.startswith(expected_first_point), msg="First point of responsibilities doesn't match.")
        expected_last_point = "- Lead and collaborate on research projects within a globally based team"
        self.assertTrue(responsibilities.endswith(expected_last_point), msg="Last point of responsibilities doesn't match.")

    def test_required_stuff_extraction(self):
        '''Test for successful extraction for required_stuff'''
        parser = FacebookParser(self.HTML_CONTENT)
        required_stuff = parser.get_job_metadata()['required_stuff']
        expected_first_point = "- Experience holding a faculty, industry, or government researcher position"
        self.assertTrue(required_stuff.startswith(expected_first_point), msg="First point of required stuff doesn't match.")
        expected_last_point = "- Must obtain work authorization in country of employment at the time of hire, and maintain ongoing work authorization during employment"
        self.assertTrue(required_stuff.endswith(expected_last_point), msg="Last point of required stuff doesn't match.")

    def test_preferred_stuff_extraction(self):
        '''Test for successful extraction for preferred_stuff'''
        parser = FacebookParser(self.HTML_CONTENT)
        preferred_stuff = parser.get_job_metadata()['preferred_stuff']
        expected_first_point = "- 1+ year(s) of work experience in a university, industry, or government lab(s), in a role with primary emphasis on AI research"
        self.assertTrue(preferred_stuff.startswith(expected_first_point), msg="First point of preferred stuff doesn't match.")
        expected_last_point = "- Experience in developing and debugging in C/C++, Python, or C#"
        self.assertTrue(preferred_stuff.endswith(expected_last_point), msg="Last point of preferred stuff doesn't match.")


class TestFacebookSoftwareEngineerSystemsMlRole(unittest.TestCase):
    '''Test Facebook Career parsers for a software engineer systems ml role'''

    def setUp(self):
        '''Get html content'''
        with open('tests/facebook_software_engineer_systems_ml_role.html') as file_obj:
            self.HTML_CONTENT = file_obj.read()

    def test_title_extraction(self):
        '''Test for successful extraction of a title.'''
        parser = FacebookParser(self.HTML_CONTENT)
        title = parser.get_job_metadata()['title']
        self.assertEqual('Software Engineer, Systems ML', title)

    def test_overview_extraction(self):
        '''Test for successful extraction for introduction_content'''
        parser = FacebookParser(self.HTML_CONTENT)
        introduction_content = parser.get_job_metadata()['introduction']
        expected_start = "Facebook is seeking AI Software Engineers to join our Research & Development teams."
        self.assertTrue(introduction_content.startswith(expected_start), msg="First sentence of introduction content doesn't match.")
        expected_end = "The position will involve taking these skills and applying them to some of the most exciting and massive social data and prediction problems that exist on the web.  We are hiring in multiple locations."
        self.assertTrue(introduction_content.endswith(expected_end), msg="Last sentence of introduction content doesn't match.")

    def test_roles_and_responsibilities_extraction(self):
        '''Test for successful extraction for roles and responsibilities'''
        parser = FacebookParser(self.HTML_CONTENT)
        responsibilities = parser.get_job_metadata()['roles_and_responsibilities']
        expected_first_point = "- Apply relevant AI and machine learning techniques to build intelligent systems that improve Facebook products and experiences"
        self.assertTrue(responsibilities.startswith(expected_first_point), msg="First point of responsibilities doesn't match.")
        expected_last_point = "- Define use cases and develop methodology and benchmarks to evaluate different approaches"
        self.assertTrue(responsibilities.endswith(expected_last_point), msg="Last point of responsibilities doesn't match.")

    def test_required_stuff_extraction(self):
        '''Test for successful extraction for required_stuff'''
        parser = FacebookParser(self.HTML_CONTENT)
        required_stuff = parser.get_job_metadata()['required_stuff']
        expected_first_point = "- BS, MS or Ph.D. degree in Computer Science or related quantitative field"
        self.assertTrue(required_stuff.startswith(expected_first_point), msg="First point of required stuff doesn't match.")
        expected_last_point = "- Experience developing machine learning algorithms or infrastructure in C++ or Python"
        self.assertTrue(required_stuff.endswith(expected_last_point), msg="Last point of required stuff doesn't match.")

    def test_preferred_stuff_extraction(self):
        '''Test for successful extraction for preferred_stuff'''
        parser = FacebookParser(self.HTML_CONTENT)
        preferred_stuff = parser.get_job_metadata()['preferred_stuff']
        one_expected_point = "- Experience with distributed systems or on-device algorithm development"
        self.assertEqual(preferred_stuff, one_expected_point)


class TestFacebookVisitingScientistAiRole(unittest.TestCase):
    '''Test Facebook Career parsers for a visiting scientist AI role'''

    def setUp(self):
        '''Get html content'''
        with open('tests/facebook_visiting_scientist_ai_role.html') as file_obj:
            self.HTML_CONTENT = file_obj.read()

    def test_title_extraction(self):
        '''Test for successful extraction of a title.'''
        parser = FacebookParser(self.HTML_CONTENT)
        title = parser.get_job_metadata()['title']
        self.assertEqual('Visiting Scientist, AI', title)

    def test_overview_extraction(self):
        '''Test for successful extraction for introduction_content'''
        parser = FacebookParser(self.HTML_CONTENT)
        introduction_content = parser.get_job_metadata()['introduction']
        expected = "Facebook is seeking Visiting Scientists to join our Facebook Artificial Intelligence Research team. Term length would be considered on a case-by-case basis."
        self.assertEqual(introduction_content, expected)

    def test_roles_and_responsibilities_extraction(self):
        '''Test for successful extraction for roles and responsibilities'''
        parser = FacebookParser(self.HTML_CONTENT)
        responsibilities = parser.get_job_metadata()['roles_and_responsibilities']
        expected_point = "- Contribute research that can be applied to Facebook product development"
        self.assertEqual(responsibilities, expected_point)

    def test_required_stuff_extraction(self):
        '''Test for successful extraction for required_stuff'''
        parser = FacebookParser(self.HTML_CONTENT)
        required_stuff = parser.get_job_metadata()['required_stuff']
        expected_first_point = "- Currently holding a faculty or government researcher position"
        self.assertTrue(required_stuff.startswith(expected_first_point), msg="First point of required stuff doesn't match.")
        expected_last_point = "- Academic publications in the field of machine learning"
        self.assertTrue(required_stuff.endswith(expected_last_point), msg="Last point of required stuff doesn't match.")

    def test_preferred_stuff_extraction(self):
        '''Test for default 'Not Provided' value when preferred list wasn't available'''
        parser = FacebookParser(self.HTML_CONTENT)
        preferred_stuff = parser.get_job_metadata()['preferred_stuff']
        expected = "Not Provided"
        self.assertEqual(preferred_stuff, expected)

