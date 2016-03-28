#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Slade'
SITENAME = u"Slade == u'死累的'"
SITEURL = u"http://furiousslade.github.io/blog"
TIMEZONE = "Asia/Shanghai"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
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

PATH = u'content'
BANNER_ALL_PAGES = True
DEFAULT_LANG = u'zh'
FILENAME_METADATA = "(?P<slug>.*)"

STATIC_PATH = ['extra']
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
          ('weibo', 'http://weibo.com/slade86'),
          ('github', 'https://github.com/FuriousSlade'),
          ('qq', '175439093'),
          ('weixin', 'w12046'),
          )

MD_EXTENSIONS = (['codehilite(css_class=highlight)',
                  'extra', 'toc'])

ABOUT_ME = 'I am Slade.<br>\
            所以我一直死累的。<br>\
            现就职于扎拉斯网络科技有限公司。'

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 30

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
DISQUS_SITENAME = u'furiousslade'

# duoshuo
# DUOSHUO_SHORTNAME = 'slade'
# projects
PROJECTS = [{
    'name': 'Swain',
    'url': 'https://github.com/FuriousSlade/Swain',
    'description': 'Pelican Theme'
}]

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)
