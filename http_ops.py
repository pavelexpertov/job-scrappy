import urllib

import requests


def get_page_content(url):
    '''Return content (either HTML text or JSON) from a given URL'''
    domain_name = get_domain(url)

    if domain_name == 'google':
        url_path = urllib.parse.urlparse(url).path
        job_id = url_path.split('/')[3].split('-')[0]
        api_url_string = "https://careers.google.com/api/v2/jobs/get"
        response = requests.get(api_url_string, params={'job_name': f"jobs/{job_id}"})
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            message = f"Google URL doesn't exist: {url}"
            raise HttpOpsError(message, exc)
        return response.json()
    else:
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            message = f"HTTP request for '{domain_name}' has failed."
            raise HttpOpsError(message, exc)
        return response.text


def get_domain(url):
    '''Get domain name from a given URL'''
    return urllib.parse.urlparse(url).netloc.split('.')[-2]


class HttpOpsError(Exception):
    '''Exception for providing extra info for HTTP errors'''

    def __init__(self, message, raised_exc):
        '''constructor for constructing the message'''
        super().__init__(message + "\nRaised exception that caused it: " + str(raised_exc))
