# -*- coding: utf-8 -*-
from __future__ import print_function
import cookielib
import os
import urllib
import urllib2
import sys
import config
import requests
import re
from bs4 import BeautifulSoup

def login():
    cookie = config.COOKIE
    return cookie

def authenticate():
    try:
        session = login()
        if len(session) == 0:
            sys.exit('[!] Unable to login to LinkedIn.com')
        print '[*] Obtained new session: %s' % session
        cookies = dict(li_at=session)
    except Exception, e:
        sys.exit('[!] Could not authenticate to linkedin. %s' % e)
    return cookies

def download_file(url, file_path, file_name):
    reply = requests.get(url, stream=True)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(file_path + '/' + file_name, 'wb') as f:
        for chunk in reply.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

if __name__ == '__main__':
    cookies = authenticate()
    headers = {'Csrf-Token': 'ajax:4332914976342601831'}
    cookies['JSESSIONID'] = 'ajax:4332914976342601831'
    for instructor in config.INSTRUCTORS:
        print ''
        pages_data = config.INSTRUCTORS[instructor].split("_")
        instructor_url = 'https://www.linkedin.com/learning-api/authorCards' \
                     '?q=authorSlug&slug={0}&start={1}&count={2}'.format(instructor, pages_data[0], pages_data[1])
        # instructor_url = 'https://www.linkedin.com/learning/instructors/blinkist?u=74415068'

        print 'instructor_url : %s' % instructor_url
        r = requests.get(instructor_url, cookies=cookies, headers=headers)
        invalid_file_chars = r'[\\/*?:.,"\'<>|]'
        # print 'R Json() : %s' % r.json()
        all_course_data = r.json()['elements']
        # print 'course_name : %s' % course_name
        # course_name = re.sub(invalid_file_chars, " ", course_name).strip().encode('utf-8')
        # chapters = r.json()['elements'][0]['chapters']
        # print 'chapters : %s' % chapters
        # print '[*] Parsing "%s" course\'s chapters' % course_name
        # print '[*] [%d chapters found]' % len(chapters)
        print ''
        for course_metadata in all_course_data:
            # print '[*] {0} percent task done.'.format(all_course_data.index(course_metadata) * 100 / len(all_course_data))
            course_slug = course_metadata['slug']
            course_url = 'https://www.linkedin.com/learning-api/detailedCourses' \
                        '??fields=videos&addParagraphsToTranscript=true&courseSlug={0}&q=slugs'.format(course_slug)
            print 'course_url : %s' % course_url
            r = requests.get(course_url, cookies=cookies, headers=headers)
            invalid_file_chars = r'[\\/*?:.,"\'<>|]'
            course_name = r.json()['elements'][0]['title']
            course_name = re.sub(invalid_file_chars, " ", course_name).strip().encode('utf-8')
            chapters = r.json()['elements'][0]['chapters']
            print '[*] Parsing "%s" course\'s chapters' % course_name
            print '[*] [%d chapters found]' % len(chapters)
            for chapter in chapters:
                chapter_name = re.sub(invalid_file_chars, " ", chapter['title']).strip().encode('utf-8')
                videos = chapter['videos']
                vc = 0
                print '[*] --- Parsing "%s" chapters\'s videos' % chapter_name
                print '[*] --- [%d videos found]' % len(videos)
                for video in videos:
                    video_name = re.sub(invalid_file_chars, " ", video['title']).strip().encode('utf-8')
                    video_slug = video['slug']
                    video_url = 'https://www.linkedin.com/learning-api/detailedCourses' \
                                '?addParagraphsToTranscript=false&courseSlug={0}&q=slugs&resolution=_720&videoSlug={1}'\
                        .format(course_slug, video_slug)
                    r = requests.get(video_url, cookies=cookies, headers=headers)
                    vc += 1
                    url_link = re.search('"progressiveUrl":"(.+)","expiresAt"', r.text).group(1)
                    try:
                        download_url = re.search('"progressiveUrl":"(.+)","expiresAt"', r.text).group(1)
                        # print '[*] Downloading from URL "%s"' % download_url
                    except:
                        print '[!] ------ Can\'t download the video "%s", probably is only for premium users' % video_name
                    else:
                        print '[*] ------ Downloading video "%s"' % video_name
                        download_file(download_url, 'LinkedInLearning-DLs/%s/%s/%s' % (config.LOCATION, course_name, chapter_name), '%s. %s.mp4' %
                                    (str(vc), video_name))
            print '█' * (all_course_data.index(course_metadata) * 100 / len(all_course_data)),
            print '-- {0}%'.format((all_course_data.index(course_metadata)+1) * 100 / len(all_course_data))
            