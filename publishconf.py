#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Slade'
SITENAME = u"Slade == u'死累的'"
SITESUBTITLE = '<i class="fa fa-copyright" aria-hidden="true"> qi.wang</i>'
SITEURL = "http://chihiro.moe"
TIMEZONE = "Asia/Shanghai"
LOCALE = ('usa', 'en_US')
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DELETE_OUTPUT_DIRECTORY = True

ARTICLE_URL = 'posts/{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

DISPLAY_CATEGORIES_ON_SIDEBAR = True
LOAD_CONTENT_CACHE = False

PATH = 'content'
BANNER_ALL_PAGES = True
DEFAULT_LANG = 'zh'
FILENAME_METADATA = "(?P<slug>.*)"

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set theme
THEME = 'pelican-swain'
DIRECT_TEMPLATES = (
    ('index', 'tags', 'categories', 'archives', '404', 'search'))


RECENT_ARTICLES_COUNT = 10

SOCIAL = (('email', 'mailto:175439093@qq.com'),
          )

MD_EXTENSIONS = (['codehilite(css_class=highlight)',
                  'extra', 'toc'])

ABOUT_ME = '''
          <h4 style="margin-top: 0px">Lv: 7</h4>
          <h5>Exp: 30/100</h5>
          <strong>Hp: 10/100</strong><br/>
          <strong>Mp: 1/25</strong><br/>
          <strong>Str: 1</strong><br/>
          <strong>Int: -5</strong><br/>
          <strong>Luk: 0</strong><br/>
          '''

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 25

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = False

RELATED_POSTS_MAX = 3

# plugin config
PLUGIN_PATHS = [u'./pelican-plugins']
PLUGINS = [
    'sitemap',
    'gzip_cache',
    'extract_toc',
    'tipue_search',
    'related_posts',
]


# sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# disqus
DISQUS_SITENAME = 'furiousslade'

# duoshuo
# DUOSHUO_SHORTNAME = 'chihiro'

# projects
# PROJECTS = [{
#     'name': 'Swain',
#     'url': 'https://github.com/FuriousSlade/Swain',
#     'description': 'Pelican Theme'
# }]

# Blogroll
LINKS = (('importcjj', 'http://www.importcjj.com/'),
         ('oreki.moe', 'http://oreki.moe/'),)

GOOGLE_ANALYTICS = 'UA-75717198-1'
BAIDU_TONGJI = '903bed5b17c3ef49f843500c8cb1a1b0'
