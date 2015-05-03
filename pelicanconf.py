#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


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

PYGMENTS_STYLE = "default"

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

STATIC_PATHS = ['images', 'downloads']

DISPLAY_PAGES_ON_MENU = True
HIDE_SIDEBAR = True

PLUGIN_PATH = "pelican-plugins"
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')


DEFAULT_PAGINATION = False 

DEFAULT_DATE_FORMAT = "%d %B %Y"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
