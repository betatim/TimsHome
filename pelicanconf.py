#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

CACHE_CONTENT = False
IGNORE_FILES = ['.#*',
                "*-checkpoint.ipynb",
                "*~"]

THEME = "simplez"

AUTHOR = u'Tim Head'
SITENAME = u"Tim Head"
SITEURL = '//betatim.github.io'

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

thebe_files = ["thebe.css", "notebookexec.js", "js-yaml.min.js",
               "main-built.js", "marked.min.js", "tesseract.css"]

STATIC_PATHS = ['images', 'downloads',
                's/interactive.txt'] + ["s/"+f for f in thebe_files]
EXTRA_PATH_METADATA = {'s/interactive.txt': {'path': 'interactive/index.html'},
                   }
EXTRA_PATH_METADATA.update(dict((("s/"+f, {'path': 'interactive/'+f})
                                 for f in thebe_files)))

DISPLAY_PAGES_ON_MENU = True
HIDE_SIDEBAR = True

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'


DEFAULT_PAGINATION = False

DEFAULT_DATE_FORMAT = "%d %B %Y"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
