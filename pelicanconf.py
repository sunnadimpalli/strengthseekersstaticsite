#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sundar Nadimpalli'
SITENAME = 'Strength Seekers'
SITEURL = 'http://www.strengthseekers.network'

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Author's Website", 'http://www.sundarnadimpalli.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/SunNadimpalli'),
          ('LinkedIn', 'https://www.linkedin.com/in/sundarnadimpalli/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'Darkly'
PYGMENTS_STYLE = 'colorful'

PLUGIN_PATHS = ['pelican-plugins']
JINJA_ENVIRONMENT = {'extensions':['jinja2.ext.i18n']}
PLUGINS = ['i18n_subsites']
I18N_TEMPLATES_LANG = 'en'