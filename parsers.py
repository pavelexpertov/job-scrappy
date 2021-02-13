import logging

import bs4


def parse_content(domain_name, content):
    '''Return a dict with parsed content'''

    if domain_name == 'google':
        return GoogleParser(content).get_job_metadata()
    elif domain_name == 'ibm':
        return IbmParser(content).get_job_metadata()
    elif domain_name == 'facebook':
        return FacebookParser(content).get_job_metadata()
    elif domain_name == 'bloomberg':
        return BloombergParser(content).get_job_metadata()
    else:
        raise ValueError(f"'{domain_name}' is not one of available parsers.")

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
        content = json_data['description'].replace('<p>', '\n')
        self.introduction_content = content.replace('</p>', '')

        soup = bs4.BeautifulSoup(json_data['responsibilities'], features="lxml")
        responsibilities = "\n".join(["- " + line.strip() for line in soup.stripped_strings])
        self.roles_and_responsibilities = responsibilities
        soup = bs4.BeautifulSoup(json_data['qualifications'], features="lxml")
        required_ul_list = soup.find('p', string="Minimum qualifications:").next_sibling()
        self.required_stuff = "\n".join(["- " + line.get_text() for line in required_ul_list])
        preferred_ul_list = soup.find('p', string="Preferred qualifications:").next_sibling()
        self.preferred_stuff = "\n".join(["- " + line.get_text() for line in preferred_ul_list])


class BloombergParser(Parser):
    '''Parser class for Bloomberg jobs'''

    def __init__(self, page_content_str):
        '''Expects HTML page string.'''
        soup = bs4.BeautifulSoup(page_content_str, features="lxml")

        div_job_name_title_tag = soup.find('div', class_="job-name-title")
        self.title = div_job_name_title_tag.h2.get_text()

        div_parent = soup.find(id="we-ll-trust-you-to").parent
        # Extracting introduction content
        text_list = []
        for tag in div_parent.children:
            if tag.name != 'h3':
                try:
                    text_list.append(tag.get_text())
                except AttributeError:
                    logging.debug("BloombergParser: A tag didn't have 'get_text' function attribute")
            else:
                break
        self.introduction_content = "\n".join(text_list)

        # Finding whether more-about-us section exists and if it does,
        # assign it to roles and responsibilities
        more_about_us_id = div_parent.find(id="more-about-us")
        if more_about_us_id:
            text_list = []
            for tag in more_about_us_id.next_siblings:
                if tag.name != 'h3':
                    try:
                        text_list.append(tag.get_text())
                    except AttributeError:
                        logging.debug("BloombergParser: A tag didn't have 'get_text' function attribute")
                else:
                    break
            self.roles_and_responsibilities = "\n".join(text_list)
        else:
            self.roles_and_responsibilities = ''

        # Finding "in-the-upcoming-year,-you..." id and if found,
        # Attach it to the roles_and_responsibilities
        id_of_interest = "in-the-upcoming-year,-you-should-expect-to-work-on-the-following"
        in_the_upcoming_year_id = div_parent.find(id=id_of_interest)
        if in_the_upcoming_year_id:
            text_list = []
            # Problem's here
            for tag in in_the_upcoming_year_id.next_siblings:
                if tag.name != 'h3':
                    try:
                        text_list.append(tag.get_text())
                    except AttributeError:
                        logging.debug("BloombergParser: A tag didn't have 'get_text' function attribute")
                else:
                    break
            content = "\n".join(text_list)
            if self.roles_and_responsibilities:
                self.roles_and_responsibilities += "\n" + content
            else:
                self.roles_and_responsibilities = content

        # Finding required stuff
        you_ll_need_to_have_id_tag = div_parent.find(id="you-ll-need-to-have")
        if you_ll_need_to_have_id_tag:
            ul_tag = you_ll_need_to_have_id_tag.find_next_sibling('ul')
            text_list = []
            self.required_stuff = "\n".join([line for line in ul_tag.stripped_strings])
        else:
            self.required_stuff = ''

        # Finding preferred stuff, if it exists, assign it to preferred_stuff
        we_d_love_to_see_id_tag = div_parent.find(id="we-d-love-to-see")
        if we_d_love_to_see_id_tag:
            ul_tag = we_d_love_to_see_id_tag.find_next_sibling('ul')
            self.preferred_stuff = "\n".join([line for line in ul_tag.stripped_strings])
        else:
            self.preferred_stuff = ''


class FacebookParser(Parser):
    '''Parser for extracting details from Facebook career pages'''

    def __init__(self, page_content_str):
        '''Expects HTML content'''

        soup = bs4.BeautifulSoup(page_content_str, features="lxml")
        self.title = soup.find('div', class_=["_9ata","_8ww0"]).get_text()

        content_div_tag = soup.find('div', class_="_8muv")

        self.introduction_content = content_div_tag.find('div', class_="_1n-_ _6hy- _94t2").get_text()

        responsibilities_div_tag = content_div_tag.find('div', string=self.title + " Responsibilities")
        minimum_qualifications_div_tag = content_div_tag.find('div', string="Minimum Qualifications")
        preferred_qualifications_div_tag = content_div_tag.find('div', string="Preferred Qualifications")

        tag_of_interest = responsibilities_div_tag.next_sibling
        self.roles_and_responsibilities = "\n".join(self._parse_ul_tag(tag_of_interest.find('ul')))

        tag_of_interest = minimum_qualifications_div_tag.next_sibling
        self.required_stuff = "\n".join(self._parse_ul_tag(tag_of_interest.find('ul')))

        if preferred_qualifications_div_tag:
            tag_of_interest = preferred_qualifications_div_tag.next_sibling
            self.preferred_stuff = "\n".join(self._parse_ul_tag(tag_of_interest.find('ul')))
        else:
            self.preferred_stuff = "Not Provided"

    def _parse_ul_tag(self, ul_tag_parser):
        '''Return a list of parsed list items from a `ul` tag'''
        return ["- " + line.get_text() for line in ul_tag_parser]
