#-----------------------------------------------------------
#-----------------------------------------------------------
# test file for Isaac Marquez's unit 2
# this file will be testing the functionality of extractor.py
# this is the main file to handle subtitiles, and this test
# file will test the functionality on youtube.com
#-----------------------------------------------------------
#-----------------------------------------------------------



# coding: utf-8

from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest     #we will be using the unittest library for our  automated testing 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#import necessary dependencies
from youtube_dl.extractor import YoutubeIE

#get their fake youtube download from their test helper file
from test.helper import FakeYDL, md5


#main test that test we get valid subtitles from youtube
#the set up of the fake youtube download was derived from
#the reposiotries files
class testSubtitles(unittest.TestCase):
    url = None
    IE = None

    #set up the youtube download download the video
    def setUp(self):
        self.DL = FakeYDL()
        self.ie = self.IE()
        self.DL.add_info_extractor(self.ie)

    #extract the info from the download
    def getInfoDict(self):
        info_dict = self.DL.extract_info(self.url, download=False)
        return info_dict

    #finally get the subtitles from the video 
    def getSubtitles(self):
        info_dict = self.getInfoDict()
        subtitles = info_dict['requested_subtitles']
        if not subtitles:
            return subtitles
        for sub_info in subtitles.values():
            if sub_info.get('data') is None:
                uf = self.DL.urlopen(sub_info['url'])
                sub_info['data'] = uf.read().decode('utf-8')
        return dict((l, sub_info['data']) for l, sub_info in subtitles.items())



    #--------------------------- test cases ----------------------------------

    #final configuration of youtube page
    url = 'QRS8MkLhQmM'
    IE = YoutubeIE


    #-------test1: test that the subtitles have been extracted--------
    def test_extraction(self):

        #get all the subtites in a variable
        self.DL.params['writesubtitles'] = True
        self.DL.params['allsubtitles'] = True
        subtitles = self.getSubtitles()

        #test that the subtitles are in english and proper format
        self.assertEqual(md5(subtitles['en']), 'ae1bd34126571a77aabd4d276b28044d')
        self.assertEqual(md5(subtitles['it']), '0e0b667ba68411d88fd1c5f4f4eab2f9')



    #-------test2: test that the subtitles are correct language--------
    def test_language(self):

        #get all the subtites in a variable
        self.DL.params['writesubtitles'] = True
        self.DL.params['allsubtitles'] = True
        subtitles = self.getSubtitles()

        #test that the subtitles are not in any other language
        for lang in ['fr', 'de']:
            self.assertTrue(subtitles.get(lang) is not None, 'Subtitles for \'%s\' not extracted' % lang)


    #-------test3: test the auto captions--------
    def test_auto_captions(self):

        #get all the subtitiles inthe variable
        self.DL.params['writeautomaticsub'] = True
        self.DL.params['subtitleslangs'] = ['it']
        subtitles = self.getSubtitles()

        #test the automic capitions
        #self.assertTrue(subtitles['it'] is not None)



    #-------test4: test that chaning the format works properly--------
    def test_format(self):

        #get all the subtitles in a variable
        self.DL.params['writesubtitles'] = True
        self.DL.params['subtitlesformat'] = 'ttml'
        subtitles = self.getSubtitles()

        #assert that the format is still correct 
        self.assertEqual(md5(subtitles['en']), 'c97ddf1217390906fa9fbd34901f3da2')

        #get all the subtitles in a variable
        self.DL.params['writesubtitles'] = True
        self.DL.params['subtitlesformat'] = 'vtt'
        subtitles = self.getSubtitles()

        #assert that the format is still correct for vtt
        self.assertEqual(md5(subtitles['en']), 'c97dadgadf1217390906fa9fbd34901f3da2')


#allow to be called from command line
if __name__ == '__main__':
    unittest.main()