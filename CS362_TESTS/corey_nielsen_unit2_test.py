#Corey Nielsen's part for CS 362 Assignment 4 
#This file will be testing the parse_duration function in utils.py

from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest     #we will be using the unittest library for our  automated testing 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#import necessary dependencies
from youtube_dl.utils import parse_duration

class TestUtilsFunctions(unittest.TestCase):

    # Testing various number formats of time
    def test_parse_duration_number_format(self):
        self.assertEqual(parse_duration('14243'), 14243)
        self.assertEqual(parse_duration('00:07:00'), 420)
        self.assertEqual(parse_duration('09:00'), 540)
        self.assertEqual(parse_duration('09:00:00'), 32400)
    
    # Testing various h m s formats
    def test_parse_duration_hms(self):
        self.assertEqual(parse_duration('2345s'), 2345)
        self.assertEqual(parse_duration('3m'), 180)
        self.assertEqual(parse_duration('1h'), 3600)
        self.assertEqual(parse_duration('3h5m2s'), 11102)
        self.assertEqual(parse_duration('3 h 5 m 2 s'), 11102)
        self.assertEqual(parse_duration('1h 1m 1s'), 3661)
        self.assertEqual(parse_duration('1h 1m1s'), 3661)
        
    # Testing various hour minute second formats
    def test_parse_duration_hoursminutesseconds(self):
        self.assertEqual(parse_duration('3 hours 5 minutes 2 seconds'), 11102)
        self.assertEqual(parse_duration('1hour1minute1second'), 3661)
        self.assertEqual(parse_duration('3hours 5minutes 2seconds'), 11102)
        self.assertEqual(parse_duration('3hours 5minutes2seconds'), 11102)

    # Testing various no input formats
    def test_parse_duration_noinput(self):
        self.assertEqual(parse_duration(''), 0)
        self.assertEqual(parse_duration('Unknown'), None)
        self.assertEqual(parse_duration('whatgoeshere'), None)

    #testing large number
    def test_parse_duration_largeinput(self):
        self.assertEqual(parse_duration('12345678912345678912481639176'), 12345678912345678912481639176)


#allow to be called from command line
if __name__ == '__main__':
    unittest.main()
