#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'nwcpp'
SITENAME = u"Northwest C++ Users’ Group"
SITEURL = 'http://nwcpp.org'
THEME = 'theme'
CSS_FILE = 'nwcpp.css'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  ((u'Standard C++ Foundation', 'http://isocpp.org/'),
          (u'Sutter’s Mill', 'http://herbsutter.com/'),
          (u'Visual C++ Team Blog', 'http://blogs.msdn.com/b/vcblog/'),
          (u'Bartosz Milewski', 'http://bartoszmilewski.com/'),
          (u'Walter Bright', 'http://www.drdobbs.com/author/Walter-Bright'),
          (u'C++ Soup!', 'http://www.cplusplus-soup.com/'),
          (u'Dr. Dobb’s C++', 'http://www.drdobbs.com/cpp'),
          (u'C++Next', 'http://cpp-next.com/'),
          (u'Scott Meyers', 'http://scottmeyers.blogspot.com/'),
          (u'Thinking Asynchronously in C++', 'http://blog.think-async.com/'),
          (u'Anthony Williams', 'http://www.justsoftwaresolutions.co.uk/cplusplus/'),
          (u'Danny Kalev', 'http://www.informit.com/authors/bio.aspx?a=e19aded6-574c-4c46-8511-101f9f0ed8f8'),
         )

# Social widget
SOCIAL = ((u'Announcements', 'http://groups.google.com/group/NwcppAnnounce'),
          (u'Volunteers List', 'http://groups.google.com/group/nwcpp-volunteers'),
          (u'Twitter', 'https://twitter.com/nwcpp'),
          (u'Facebook', 'https://www.facebook.com/groups/344125680930/'),
          (u'YouTube', 'http://www.youtube.com/user/NWCPP'),
          (u'Vimeo', 'http://vimeo.com/nwcpp'),
          (u'LinkedIn', 'http://www.linkedin.com/groups?gid=2770106'),
          (u'Speaker Deck', 'https://speakerdeck.com/nwcpp'),
          (u'SlideShare', 'http://www.slideshare.net/nwcpp'),
         )

CONFERENCE_LINKS = ((u'CPPCon Homepage', 'http://cppcon.org'),
                    (u'CPPCon Registration', 'http://cppcon.org/registration/'),
                    (u'Other C++ conferences', 'https://isocpp.org/wiki/faq/conferences-worldwide/'))

					
# job links
JOB_LINKS = ((u'Protingent', 'protingent_masthead_logo_new.png', 'http://jobs.protingent.com/'),
             (u'Volt', 'Volt.jpg', 'https://jobs.volt.com'),
             (u'Triple Crown', 'TripleCrown.jpg', 'https://www.tripleco.com/find-tech-jobs/'),
             (u'John Galt', 'JohnGalt.jpg', 'https://j-galt.com/'))

# sponsors
SPONSOR_LINKS = ((u'Cyber Data', 'CyberDataLogo.jpg', 'http://www.cyberdata-robotics.com/'),
                 (u'Microsoft', 'MSLogo.png', 'https://aka.ms/cpp'))

ANNOUNCEMENT_LINKS = ((u'There are no announcements at this time.', u'', '', u''),
						)
					
					
DEFAULT_PAGINATION = 12

PATH = 'content'
STATIC_PATHS = ['talks', 'images', 'extras']

# Do not process .html files; e.g., Bartosz's 2007 slides
READERS = {'html': None}

EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/CNAME': {'path': 'CNAME'},
}
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
