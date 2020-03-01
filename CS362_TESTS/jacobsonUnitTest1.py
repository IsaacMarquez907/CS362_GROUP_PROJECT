#!/usr/bin/env python
# coding: utf-8

# import necessary libraries
import os
import sys
import unittest
#allow the script to be run directly
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#import function to test
from youtube_dl.utils import sanitize_url

#unit test for the sanitize_url function
#function takes a url standardizes it for consistency
class test_util_sanitize_url(unittest.TestCase):
    #test base case, no fix needed
    def test_sanitize_url_base_case (self):
        self.assertEqual(sanitize_url('http//:google.com'), 'http//:google.com')
    #test to see if the fucntion preprends http://  
    def test_no_prefix_sanitize_url (self):
        self.assertEqual(sanitize_url('google.com'), 'http://google.com')
    #test to check for a common mistake of fogetting a colon
    def test_no_colon_prefix_sanitize_url (self):
        self.assertEqual(sanitize_url('http//google.com'), 'http://google.com')
    #test to check if www prefix is formatted correctly
    def test_full_prefix_sanitize_url (self):
        self.assertEqual(sanitize_url('www.google.com'), 'www.google.com')
    #Test the slash expansion functionality 
    def test_sanitize_url_slash_expansion(self):
        self.assertEqual(sanitize_url('//google.com'), 'http://google.com')

if __name__ == '__main__':
    unittest.main()
