#-----------------------------------------------------------
#-----------------------------------------------------------
# test file for Isaac Marquez's unit 1
# this file will be testing the functionality of options.py
# there are main functions within this file that the main
# youtubeDL calls and handles sensitive information
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
from youtube_dl.options import _hide_login_info
from youtube_dl.options import parseOpts


#main test to test multiple of the options within the options file
#not all of these test are on functions within the options.py file
class TestOptions(unittest.TestCase):

    #-------test1: test functionailty of the hide login info functin--------
    def test_hide_login_info(self):

        #make sure it sets the username and password as private
        self.assertEqual(_hide_login_info(['-u', 'foo', '-p', 'bar']),
                         ['-u', 'PRIVATE', '-p', 'PRIVATE'])

        #if there is no info, it shouldn't add any                   
        self.assertEqual(_hide_login_info(['-u']), ['-u'])

        #if given two usernames, they should still be private
        self.assertEqual(_hide_login_info(['-u', 'foo', '-u', 'bar']),
                         ['-u', 'PRIVATE', '-u', 'PRIVATE'])

        #test if user name is given in different from, it is still private
        self.assertEqual(_hide_login_info(['--username=foo']),
                         ['--username=PRIVATE'])




    #-------test2: test to parse the header information--------
    def test_parseOpts(self):
        
        #make sure all of the flags are intitiailzed as their proper values
        temp = parseOpts(['-u', 'foo', '-p', 'bar'])
        self.assertEqual(temp[1], {'cn_verification_proxy': None, 'keepvideo': False, 'dump_user_agent': False, 'http_chunk_size': None, 'prefer_ffmpeg': None, 'debug_printtraffic': False, 'autonumber': False, 'datebefore': None, 'dump_intermediate_pages': False, 'write_all_thumbnails': False, 'extractaudio': False, 'age_limit': None, 'min_filesize': None, 'audioquality': u'5', 'listformats': None, 'nopostoverwrites': False, 'youtube_include_dash_manifest': True, 'format': None, 'videopassword': None, 'getid': False, 'hls_use_mpegts': None, 'no_warnings': False, 'playliststart': 1, 'password': u'bar', 'max_views': None, 'update_self': None, 'gettitle': False, 'geo_bypass_ip_block': None, 'min_views': None, 'getthumbnail': False, 'metafromtitle': None, 'nooverwrites': False, 'no_check_certificate': False, 'matchtitle': None, 'progress_with_newline': False, 'writethumbnail': False, 'dump_single_json': False, 'ignore_config': None, 'embedthumbnail': False, 'geo_verification_proxy': None, 'ffmpeg_location': None, 'writeautomaticsub': False, 'list_extractors': False, 'prefer_insecure': None, 'print_json': False, 'noprogress': False, 'embedsubtitles': False, 'cachedir': None, 'proxy': None, 'cookiefile': None, 'updatetime': True, 'getformat': False, 'quiet': False, 'outtmpl': None, 'youtube_print_sig_code': False, 'write_pages': False, 'writesubtitles': False, 'external_downloader_args': None, 'dumpjson': False, 'buffersize': u'1024', 'postprocessor_args': None, 'listsubtitles': False, 'skip_download': False, 'encoding': None, 'sleep_interval': None, 'rm_cachedir': None, 'ap_list_mso': False, 'autonumber_size': None, 'mark_watched': False, 'load_info_filename': None, 'nopart': False, 'ap_mso': None, 'verbose': False, 'ap_username': None, 'ignoreerrors': False, 'default_search': None, 'autonumber_start': 1, 'include_ads': None, 'writeannotations': False, 'playlist_items': None, 'skip_unavailable_fragments': True, 'no_color': False, 'username': u'foo', 'bidi_workaround': None, 'geturl': False, 'xattr_set_filesize': None, 'max_downloads': None, 'ap_password': None, 'referer': None, 'simulate': False, 'usetitle': False, 'fragment_retries': 10, 'getfilename': False, 'retries': 10, 'subtitleslangs': [], 'subtitlesformat': u'best', 'writeinfojson': False, 'convertsubtitles': None, 'headers': None, 'batchfile': None, 'getduration': False, 'noplaylist': False, 'geo_bypass': True, 'xattrs': False, 'external_downloader': None, 'socket_timeout': None, 'rejecttitle': None, 'geo_bypass_country': None, 'max_filesize': None, 'ratelimit': None, 'extract_flat': False, 'audioformat': u'best', 'playlist_reverse': None, 'download_archive': None, 'user_agent': None, 'max_sleep_interval': None, 'exec_cmd': None, 'twofactor': None, 'noresizebuffer': False, 'merge_output_format': None, 'allsubtitles': False, 'writedescription': False, 'consoletitle': False, 'test': False, 'fixup': u'detect_or_warn', 'source_address': None, 'useid': False, 'call_home': False, 'usenetrc': False, 'addmetadata': False, 'playlistend': None, 'dateafter': None, 'date': None, 'force_generic_extractor': False, 'restrictfilenames': False, 'match_filter': None, 'playlist_random': None, 'keep_fragments': False, 'continue_dl': True, 'prefer_free_formats': False, 'config_location': None, 'list_extractor_descriptions': False, 'getdescription': False, 'list_thumbnails': False, 'recodevideo': None, 'hls_prefer_native': None})

        #make sure the arugments result is still zero
        temp = parseOpts(['-u', 'foo', '-p', 'bar'])
        self.assertEqual(temp[2], [])




    #-------test3: test to parse the header information--------
    def test_parseOpts_emptyInput(self):
        
        #make sure all of the flags are intitiailzed as their proper values
        temp = parseOpts()
        self.assertEqual(temp[1], {'cn_verification_proxy': None, 'keepvideo': False, 'dump_user_agent': False, 'http_chunk_size': None, 'prefer_ffmpeg': None, 'debug_printtraffic': False, 'autonumber': False, 'datebefore': None, 'dump_intermediate_pages': False, 'write_all_thumbnails': False, 'extractaudio': False, 'age_limit': None, 'min_filesize': None, 'audioquality': u'5', 'listformats': None, 'nopostoverwrites': False, 'youtube_include_dash_manifest': True, 'format': None, 'videopassword': None, 'getid': False, 'hls_use_mpegts': None, 'no_warnings': False, 'playliststart': 1, 'password': None, 'max_views': None, 'update_self': None, 'gettitle': False, 'geo_bypass_ip_block': None, 'min_views': None, 'getthumbnail': False, 'metafromtitle': None, 'nooverwrites': False, 'no_check_certificate': False, 'matchtitle': None, 'progress_with_newline': False, 'writethumbnail': False, 'dump_single_json': False, 'ignore_config': None, 'embedthumbnail': False, 'geo_verification_proxy': None, 'ffmpeg_location': None, 'writeautomaticsub': False, 'list_extractors': False, 'prefer_insecure': None, 'print_json': False, 'noprogress': False, 'embedsubtitles': False, 'cachedir': None, 'proxy': None, 'cookiefile': None, 'updatetime': True, 'getformat': False, 'quiet': False, 'outtmpl': None, 'youtube_print_sig_code': False, 'write_pages': False, 'writesubtitles': False, 'external_downloader_args': None, 'dumpjson': False, 'buffersize': u'1024', 'postprocessor_args': None, 'listsubtitles': False, 'skip_download': False, 'encoding': None, 'sleep_interval': None, 'rm_cachedir': None, 'ap_list_mso': False, 'autonumber_size': None, 'mark_watched': False, 'load_info_filename': None, 'nopart': False, 'ap_mso': None, 'verbose': False, 'ap_username': None, 'ignoreerrors': False, 'default_search': None, 'autonumber_start': 1, 'include_ads': None, 'writeannotations': False, 'playlist_items': None, 'skip_unavailable_fragments': True, 'no_color': False, 'username': None, 'bidi_workaround': None, 'geturl': False, 'xattr_set_filesize': None, 'max_downloads': None, 'ap_password': None, 'referer': None, 'simulate': False, 'usetitle': False, 'fragment_retries': 10, 'getfilename': False, 'retries': 10, 'subtitleslangs': [], 'subtitlesformat': u'best', 'writeinfojson': False, 'convertsubtitles': None, 'headers': None, 'batchfile': None, 'getduration': False, 'noplaylist': False, 'geo_bypass': True, 'xattrs': False, 'external_downloader': None, 'socket_timeout': None, 'rejecttitle': None, 'geo_bypass_country': None, 'max_filesize': None, 'ratelimit': None, 'extract_flat': False, 'audioformat': u'best', 'playlist_reverse': None, 'download_archive': None, 'user_agent': None, 'max_sleep_interval': None, 'exec_cmd': None, 'twofactor': None, 'noresizebuffer': False, 'merge_output_format': None, 'allsubtitles': False, 'writedescription': False, 'consoletitle': False, 'test': False, 'fixup': u'detect_or_warn', 'source_address': None, 'useid': False, 'call_home': False, 'usenetrc': False, 'addmetadata': False, 'playlistend': None, 'dateafter': None, 'date': None, 'force_generic_extractor': False, 'restrictfilenames': False, 'match_filter': None, 'playlist_random': None, 'keep_fragments': False, 'continue_dl': True, 'prefer_free_formats': False, 'config_location': None, 'list_extractor_descriptions': False, 'getdescription': False, 'list_thumbnails': False, 'recodevideo': None, 'hls_prefer_native': None}
)


        #make sure the arugments result is still zero
        temp = parseOpts()
        self.assertEqual(temp[2], [])

        #test that the instances of the parser still runs
        temp = parseOpts()
        self.assertGreaterEqual(temp[0], "optparse.OptionParse at 0x7f9f584d1d20")



#allow to be called from command line
if __name__ == '__main__':
    unittest.main()
