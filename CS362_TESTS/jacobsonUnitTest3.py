#!/usr/bin/env python
# coding: utf-8

# import necessary libraries
import os
import sys
import unittest
#allow the script to be run directly
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#import function to test
from youtube_dl.utils import formatSeconds

#Unit test designed to test the seconds formatting function found in the util.py script
#funtion takes in a value in seconds and formats the output
class test_format_seconds(unittest.TestCase):
    #test a standard sub one minute input
    def test_format_seconds_under_minute (self):
        self.assertEqual(formatSeconds(30), '30')
    #test an edge case of exactly 60 seconds
    def test_format_seconds_one_minute (self):
        self.assertEqual(formatSeconds(60), '60')
    #test minute formatting
    def test_format_seconds_one_minute (self):
        self.assertEqual(formatSeconds(61), '1:01')
    def test_format_seconds_ten_minutes (self):
    #test double digit minute formatting
        self.assertEqual(formatSeconds(600), '10:00')
    #test extreme case if 24 hours
    def test_format_second_24_hours (self):
        self.assertEqual(formatSeconds(86400), '24:00:00')

if __name__ == '__main__':
    unittest.main()