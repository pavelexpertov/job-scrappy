import unittest
from unittest.mock import patch

import http_ops

class TestGetDomainFunction(unittest.TestCase):
    '''Test http_ops.get_domain function'''

    def test_for_google(self):
        '''Test for successful extraction of Google domain'''
        url = "https://careers.google.com/jobs/results/85810091258716870-data-science-lead-google-maps-core-metrics/?q=artificial%20intelligence"
        returned_domain = http_ops.get_domain(url)
        self.assertEqual(returned_domain, 'google')

    def test_for_bloomberg(self):
        '''Test for successful extraction of Bloomberg domain'''
        url = "https://careers.bloomberg.com/job/detail/87013"
        returned_domain = http_ops.get_domain(url)
        self.assertEqual(returned_domain, 'bloomberg')

    def test_for_ibm(self):
        '''Test for successful extraction of IBM domain'''
        url = "https://careers.ibm.com/ShowJob/Id/1060432/AI-Research-Engineer-Future-of-Computing-(12-Month-Internship)/"
        returned_domain = http_ops.get_domain(url)
        self.assertEqual(returned_domain, 'ibm')

    def test_for_facebook(self):
        '''Test for successful extraction of Facebook domain'''
        url = "https://www.facebook.com/careers/v2/jobs/500751954278204/"
        returned_domain = http_ops.get_domain(url)
        self.assertEqual(returned_domain, 'facebook')


@patch("http_ops.requests", spec_set=True, name="requests_mod_mock")
class TestGetPageContent(unittest.TestCase):
    '''Test http_ops.get_page_content function'''

    def test_correct_request_for_google(self, requests_mod_mock):
        '''Test for correct arguments for 'requests' when targeting Google'''
        url = "https://careers.google.com/jobs/results/11122233344455566-data-science-lead-google-maps-core-metrics/?q=artificial%20intelligence"
        http_ops.get_page_content(url)
        requests_mod_mock.get.assert_called_once_with(
            "https://careers.google.com/api/v2/jobs/get",
            params={'job_name': "jobs/11122233344455566"}
        )

    def test_correct_request_for_ibm(self, requests_mod_mock):
        '''Test for correct arguments for 'requests' when targeting IBM'''
        url = "https://careers.ibm.com/ShowJob/Id/1060432/AI-Research-Engineer-Future-of-Computing-(12-Month-Internship)/"
        http_ops.get_page_content(url)
        requests_mod_mock.get.assert_called_once_with(url)

    def test_correct_request_for_facebook(self, requests_mod_mock):
        '''Test for correct arguments for 'requests' when targeting Facebook'''
        url = "https://www.facebook.com/careers/v2/jobs/500751954278204/"
        http_ops.get_page_content(url)
        requests_mod_mock.get.assert_called_once_with(url)

    def test_correct_request_for_bloomberg(self, requests_mod_mock):
        '''Test for correct arguments for 'requests' when targeting Bloomberg'''
        url = "https://careers.bloomberg.com/job/detail/87013"
        http_ops.get_page_content(url)
        requests_mod_mock.get.assert_called_once_with(url)

