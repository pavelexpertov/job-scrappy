import urllib

import requests


def get_page_content(url):
    '''Return content (either HTML text or JSON) from a given URL'''
    domain_name = get_domain(url)

    if domain_name == 'google':
        url_path = urllib.parse.urlparse(url).path
        job_id = url_path.split('/')[3].split('-')[0]
        api_url_string = "https://careers.google.com/api/v2/jobs/get"
        response = requests.get(api_url_string, params={'job_name': job_id})
        return response.json()
    else:
        return requests.get(url).text

def get_domain(url):
    '''Get domain name from a given URL'''
    return urllib.parse.urlparse(url).netloc.split('.')[-2]
