#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


THEME = "simplez"

AUTHOR = u'Tim Head'
SITENAME = u"Tim Head"
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# No tags
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
DISPLAY_TAGS_ON_SIDEBAR = False

#DIRECT_TEMPLATES = ('index', 'archives')

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

#MENUITEMS = [('Sports', 'pages/sports.html'),
#             ('About', 'pages/about-me.html'),
#         ]

STATIC_PATHS = ['images',]

DISPLAY_PAGES_ON_MENU = True
HIDE_SIDEBAR = True

PLUGIN_PATH = "pelican-plugins"
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']


# Social widget
SOCIAL = (('twitter', 'https://twitter.com/betatim'),)

DEFAULT_PAGINATION = 10

DEFAULT_DATE_FORMAT = "%d %B %Y"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
