# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = 'heilpraktiker-frank-schneider.de'
WWW_ROOT = 'http://heilpraktiker-frank-schneider.de'

AUTHOR = 'Frank Schneider'
EMAIL = 'info@heilpraktiker-frank-schneider.de'

FILTERS = ['markdown+codehilite(css_class=highlight)', 'hyphenate', 'h1']

VIEWS = {
    '/blog/': {'filters': 'summarize', 'view': 'index',
          'pagination': '/blog/page/:num/'},

    '/blog/:year/:slug/': {'views': ['entry', 'draft']},

    '/blog/tag/:name/': {'filters': 'summarize', 'view':'tag',
                    'pagination': '/blog/tag/:name/:num/'},

    '/blog/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atom'},
    #'/blog/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rss'},

    # # per tag Atom or RSS feed. Just uncomment to generate them.
    # '/tag/:name/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atompertag'},
    # '/tag/:name/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rsspertag'},

    '/blog/articles/': {'view': 'articles', 'template': 'articles.html'},

    '/blog/sitemap.xml': {'view': 'sitemap'},

    # # Here are some more examples

    # # '/:slug/' is a slugified url of your static page's title
    '/:slug/': {'view': 'page', 'template': 'page.html'},

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    '/blog/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagges with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags},

    # # a full typography features entry including MathML and Footnotes
    # '/:year/:slug': {'filters': ['typography', 'Markdown+Footnotes+MathML'],
    #                  'view': 'entry'},

    # # translations!
    # '/:year/:slug/:lang/': {'view': 'translation'},
}

THEME = 'bootsrap_theme'
ENTRY_PERMALINK = '/blog/:year/:slug/index.html'
PAGE_PERMALINK = '/:slug/index.html'
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_START_INDEX = 0
TAG_CLOUD_SHUFFLE = False
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%d.%m.%Y, %H:%M'
DEPLOYMENT = {
    'default': 'rsync -av $OUTPUT_DIR hpfs@ursa.uberspace.de:~/html/',
    'clear_deploy': 'rsync -av --delete $OUTPUT_DIR hpfs@ursa.uberspace.de:~/html/',
}
