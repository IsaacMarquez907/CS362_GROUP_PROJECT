#------------------------------------------------------------------
#------------------------------------------------------------------
#test file for Marc Baiza's unit 2
#this file will test the functionality of utils.py and its age restriction function
#this is the main file that will test age restriction
#this will test age ranges and whether it releases the right content
#------------------------------------------------------------------
#------------------------------------------------------------------

#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Various small unit tests
import io
import json
import xml.etree.ElementTree

from youtube_dl.utils import (
    age_restricted,
    unified_timestamp,
)

from youtube_dl.compat import (
    compat_chr,
    compat_etree_fromstring,
    compat_getenv,
    compat_os_name,
    compat_setenv,
    compat_urlparse,
    compat_parse_qs,
)

#Test to test the different functions within utils.py
class TestUtil(unittest.TestCase):

#--------test 1: test the functionality of the age restriction function---------
#This will insert different age ranges and edge cases to make sure the wrong content is not getting into the users hands. 
    def test_age_restricted_unrestricted_ranges(self):
         # This first assertion tests unrestricted content
        self.assertFalse(age_restricted(None, 12)) 
        #This second assertion tests unrestricted policy
        self.assertFalse(age_restricted(1, None)) 

#--------test 2: test the functionality of the age restriction function---------
    def test_age_restricted_normal_ranges(self):
        #The rest of the assertions test other ranges and edge cases.  
        self.assertFalse(age_restricted(8, 17))
        self.assertTrue(age_restricted(18, 12))
        self.assertFalse(age_restricted(21, 21))
#-------test 3: test the functionality of the age restriction function----------
    def test_age_restricted_extreme_ranges(self):
        self.assertFalse(age_restricted(8,100000000000000000000000000000000000000000000000))
        self.assertTrue(age_restricted(1000000000000000000000000000000000000, 8))
#-------test 4: test the functionality of the age restriction function----------
    def test_age_restricted_high_ranges(self):
        self.assertFalse(age_restricted(2000, 3000))
        self.assertTrue(age_restricted(3000, 2000))
#-------test 5: test the functionality of the age restriction function----------
    def test_age_restricted_opposite_assertions(self):
        self.assertTrue(age_restricted(2000, 3000))
        self.assertFalse(age_restricted(3000, 2000))

#allow to be called from command line
if __name__ == '__main__':
    unittest.main()
