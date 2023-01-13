# -*- coding: utf-8 -*-

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

def process_download_for_course(course_name, all_course_data, course_index):
    if not course_index in config.SKIP:
        print '[*] Downloading : {0} from index {1}'.format(course_slug, course_index)
        course_url = 'https://www.linkedin.com/learning-api/detailedCourses' \
                    '??fields=videos&addParagraphsToTranscript=true&courseSlug={0}&q=slugs'.format(course_slug)
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
            print '[*] --- Parsing {0} - "{1}" chapters\'s videos'.format(int(chapters.index(chapter)+1), chapter_name)
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
                except:
                    print '[!] ------ Can\'t download the video "%s", probably is only for premium users' % video_name
                else:
                    print '[*] ------ Downloading video "%s"' % video_name
                    download_file(download_url, 'LinkedInLearning-DLs/%s/%s/%s' % (config.LOCATION, course_name, chapter_name), '%s. %s.mp4' %
                                (str(vc), video_name))
        print '[*] ',
        print '█' * (course_index * 100 / len(all_course_data)),
        print '░' * ((len(all_course_data) - course_index) * 100 / len(all_course_data)),
        print '-- {0}%'.format(course_index * 100 / len(all_course_data))
    else:
        print '[*] Not downloading {0}'.format(course_slug)

if __name__ == '__main__':
    cookies = authenticate()
    headers = {'Csrf-Token': 'ajax:4332914976342601831'}
    cookies['JSESSIONID'] = 'ajax:4332914976342601831'
    parsing_flow = config.CHOICE
    print ''
    if parsing_flow == 1:
        for instructor in config.INSTRUCTORS:
            pages_data = config.INSTRUCTORS[instructor].split("_")
            instructor_url = 'https://www.linkedin.com/learning-api/authorCards' \
                        '?q=authorSlug&slug={0}&start={1}&count={2}'.format(instructor, pages_data[0], pages_data[1])
            print '[*] instructor_url : %s' % instructor_url
            r = requests.get(instructor_url, cookies=cookies, headers=headers)
            invalid_file_chars = r'[\\/*?:.,"\'<>|]'
            all_course_data = r.json()['elements']
            for course_metadata in all_course_data:
                course_slug = course_metadata['slug']
                process_download_for_course(course_slug, all_course_data, int(all_course_data.index(course_metadata)+1))
    elif parsing_flow == 2:
        for path in config.PATHS:
            path_url = 'https://www.linkedin.com/learning-api/detailedLearningPaths' \
                        '?learningPathSlug={0}&q=slug&version=2'.format(path)

            print '[*] path_url : %s' % path_url
            r = requests.get(path_url, cookies=cookies, headers=headers)
            invalid_file_chars = r'[\\/*?:.,"\'<>|]'
            all_course_data = r.json()['elements'][0]['sections'][0]['items']
            print '[*] SKIP {0} courses from the Learning PATH'.format(config.SKIP)
            for course_metadata in all_course_data:
                course_slug = course_metadata['content']['com.linkedin.learning.api.ListedCourse']['slug']
                process_download_for_course(course_slug, all_course_data, int(all_course_data.index(course_metadata)+1))

    elif parsing_flow == 3:
        for course in config.COURSES:
            course_slug = course
            process_download_for_course(course_slug, config.COURSES, int(config.COURSES.index(course)+1))

    else:
        print '[!] Invalid choice'

