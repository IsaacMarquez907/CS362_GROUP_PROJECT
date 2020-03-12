#------------------------------------------------------------------
#------------------------------------------------------------------
#test file for Marc Baiza's unit 1
#this file will test the functionality of utils.py
#this is the main file that will test the date formatting
#this will test extracting dates from videos with different formats
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

#-------test1: test the functionality of the "unified time stamp" functionality---------
    def test_unified_timestamps(self):
    #Each serve as a different insertion for unified timestamp
        self.assertEqual(unified_timestamp('Feb 14th 2016 5:45PM'), 1455471900)
        self.assertEqual(unified_timestamp('March 15, 2017 at 7:49 am'), 1489564140)
        self.assertEqual(unified_timestamp('27.02.2016 17:30'), 1456594200)
        self.assertEqual(unified_timestamp('March 16, 2016 11:15 PM'), 1458170100)
        self.assertEqual(unified_timestamp('Sep 11, 2013 | 5:49 AM'), 1378878540)
#--------test2: Even more date formats to test the functionality------------------------- 
    def test_unified_timestamps2(self):
        self.assertEqual(unified_timestamp('8/7/2009'), 1247011200)
        self.assertEqual(unified_timestamp('2012/10/11 01:56:38 +0000'), 1349920598)
        self.assertEqual(unified_timestamp('28/01/2014 21:00:00 +0100'), 1390939200)
        self.assertEqual(unified_timestamp('11/26/2014 11:30:00 AM PST', day_first=False),1417001400)
        self.assertEqual(unified_timestamp('2/2/2015 6:47:40 PM', day_first=False),1422902860)
#--------test3: Even more date formats to test the functionality-------------------------       
    def test_unified_timestamps3(self):
        self.assertEqual(unified_timestamp('UNKNOWN DATE FORMAT'), None)
#--------test4: Even more date formats to test the functionality-------------------------
    def test_unified_timestamps4(self):
        self.assertEqual(unified_timestamp('2018-03-14T08:32:43.1493874+00:00'), 1521016363)
        self.assertEqual(unified_timestamp('1973-10-11'), 119145600)
        self.assertEqual(unified_timestamp('2018-03-30T17:52:41Q'), 1522432361)
        self.assertEqual(unified_timestamp('25-09-2014'), 1411603200)
#--------test5: Even more date formats to test the functionality-------------------------
    def test_unified_timestamps5(self):
        self.assertEqual(unified_timestamp('1973 10 11'), 119145600)
        self.assertEqual(unified_timestamp('Feb 14, 2011'), 1297641600)
        self.assertEqual(unified_timestamp('September 21, 2010'), 1285027200)
#allow to be called from command line
if __name__ == '__main__':
    unittest.main()