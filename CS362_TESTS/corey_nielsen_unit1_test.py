#Corey Nielsen's part for CS 362 Assignment 4 
#This file will be testing the month_by_name and month_by_abbreviation functions

from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest     #we will be using the unittest library for our  automated testing 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#import necessary dependencies
from youtube_dl.utils import month_by_name
from youtube_dl.utils import month_by_abbreviation

class TestUtilsFunctions(unittest.TestCase):

    def test_month_by_name_english_default(self):
        
        #checking each month outputs the correct number
        self.assertEqual(month_by_name('December'), 12)

        #checking mispelled month
        self.assertEqual(month_by_name('Octobber'), None)

        #testing no input
        self.assertEqual(month_by_name(''), None)

    def test_month_by_name_foreign_language(self):
        #testing french option
        self.assertEqual(month_by_name('mars', 'fr'), 3)

        #checking using another language when default is english
        self.assertEqual(month_by_name('mars'), None)

        #checking capitalized version
        self.assertEqual(month_by_name('Mars', 'fr'), None)

        #checking lowercase works
        self.assertEqual(month_by_name('november'), 11)

    def test_month_by_abbreviation(self):

        #testing abbreviation capitalized
        self.assertEqual(month_by_abbreviation('Jan'), 1)

        #testing lowercase abbreviation
        self.assertEqual(month_by_abbreviation('jan'), 1)

        #testing full month name
        self.assertEqual(month_by_abbreviation('January'), None)

        #testing mispelled abbreviation
        self.assertEqual(month_by_abbreviation('De'), None)

        #testing no input
        self.assertEqual(month_by_abbreviation(''), None)

    def test_large_random_text_inputs(self):
        self.assertEqual(month_by_name('jasjfdl;kasjdf;laajgj;lsadglha;osihgioahe;oisdkl fasg;lhaslkdhaskglkhaslgh;alskjfl;asgj;ahsg;'), None)
        self.assertEqual(month_by_abbreviation('alds;glas;ldhg;aa;sldf;oaisgsdfasdijf;j;ahg;ahdkhakjslhgah;igha;lsdfl;aj;lghadhg'), None)

    def test_number_inputs(self):
        self.assertEqual(month_by_name(52342645735730248582370582805723847508), None)
        self.assertEqual(month_by_abbreviation(203857027304582540283548025729384), None)




#allow to be called from command line
if __name__ == '__main__':
    unittest.main()
