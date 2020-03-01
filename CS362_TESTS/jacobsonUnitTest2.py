#!/usr/bin/env python
# coding: utf-8

# import necessary libraries
import os
import sys
import unittest
#allow the script to be run directly
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#import function to test
from youtube_dl.utils import clean_html

#Unit test for the html clean function. Funtion should remove the html formatting and just leave the plain text
class test_util_html_clean(unittest.TestCase):
    #test base case, no html
    def test_clean_html_base (self):
        self.assertEqual(clean_html('This should return the exact same text'), 'This should return the exact same text')
    #short test
    def test_clean_html_basic (self):
        self.assertEqual(clean_html('<HTML><HEAD> this is a test</HEAD><HTML>'), 'this is a test')
    #medium test
    def test_clean_html_moderate (self):
        self.assertEqual(clean_html('<HTML><HEAD><TITLE> this is a test </TITLE></HEAD><BR><P>here is a line of text</HTML>'), 'this is a test here is a line of text')
    #test to see how links are handled
    def test_clean_html_links (self):
        self.assertAlmostEqual(clean_html('<a href="http://myspace.com"> myspace </a>'), 'myspace')
    #Advanced test with a variety of tags 
    def test_clean_html_advance (self):
        self.assertEqual(clean_html('<HTML><HEAD><TITLE>TEST <TITLE></HEAD><BODY BGCOLOR="EEEEEE"><H1>this is </H1><H2>a test </H2><BR><P><BODY>checkout myspace.com<table border="1" cellpadding="10" width="80%"><img src="img_myspace.jpg" alt="myspace.com"></BODY></HTML>'), 'TEST this is a test checkout myspace.com')

if __name__ == '__main__':
    unittest.main()