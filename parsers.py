import bs4

class Parser():
    '''Base class for a parser'''

    def __init__(self):
        pass

    def get_job_metadata(self):
        '''Return dict with job's details'''
        return {
            'title': self.title,
            'introduction': self.introduction_content,
            'roles_and_responsibilities': self.roles_and_responsibilities,
            'required_stuff': self.required_stuff,
            'preferred_stuff': self.preferred_stuff
        }

class IbmParser(Parser):
    '''Parser class for IBM job websites.'''

    def __init__(self, page_content_str):
        '''page_content_str is an HTML content string'''
        soup = bs4.BeautifulSoup(page_content_str, features="lxml")
        main_job_section_tag = soup.find(attrs={'class': "job-main"})
        self.title = main_job_section_tag.h1.text

        job_desc_tag = main_job_section_tag.find(id='job-description')

        introduction_span = job_desc_tag.find('span', string='Introduction')
        self.introduction_content = introduction_span.next_sibling.next_sibling.next_sibling
        info_dict = self._parse_job_description(job_desc_tag)
        self.roles_and_responsibilities = info_dict['roles_and_responsibilities']
        self.required_stuff = info_dict['required_stuff']
        self.preferred_stuff = info_dict['preferred_stuff']

    def _parse_job_description(self, job_desc_tag):
        '''Parse through job description tag to extract specific content'''
        key_start_end_matches_list = [
            ('roles_and_responsibilities', 'Your Role and Responsibilities', 'Required Technical'),
            ('required_stuff', 'Required Technical and Professional Expertise', 'Preferred Technical'),
            ('preferred_stuff', 'Preferred Technical and Professional Expertise', 'About Business Unit')
        ]
        info_dict = {}
        for key, start_match, end_match in key_start_end_matches_list:
            text_iterator = iter(job_desc_tag.stripped_strings)
            for line in text_iterator:
                if start_match in line:
                    string_list = []
                    for line in text_iterator:
                        if end_match not in line:
                            string_list.append(line)
                        else:
                            break
                    info_dict[key] = '\n'.join(string_list)
                    break
                else:
                   continue
            else:
                raise ValueError(f"Couldn't find start match for {start_match}. Current tuple: {(key, start_match, end_match)}")
        return info_dict


class GoogleParser(Parser):
    '''Parser class for Google job websites'''

    def __init__(self, json_data):
        '''Expects a dict stucture of a return JSON data from API.'''
        self.title = json_data['title']
        self.introduction_content = json_data['description']

        soup = bs4.BeautifulSoup(json_data['responsibilities'], features="lxml")
        responsibilities = "\n".join([line for line in soup.stripped_strings])
        self.roles_and_responsibilities = responsibilities
        soup = bs4.BeautifulSoup(json_data['qualifications'], features="lxml")
        required_ul_list = soup.find('p', string="Minimum qualifications:").next_sibling()
        self.required_stuff = "\n".join(["- " + line.get_text() for line in required_ul_list])
        preferred_ul_list = soup.find('p', string="Preferred qualifications:").next_sibling()
        self.preferred_stuff = "\n".join(["- " + line.get_text() for line in preferred_ul_list])



