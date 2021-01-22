import bs4

class IbmParser():
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


    def get_job_metadata(self):
        '''Return dict with job's details'''
        return {
            'title': self.title,
            'introduction': self.introduction_content,
            'roles_and_responsibilities': self.roles_and_responsibilities
        }

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

