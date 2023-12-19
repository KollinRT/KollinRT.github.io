AUTHOR = 'KT'
SITENAME = 'Blog'
SITEURL = "https://KollinRT.github.io"

PATH = "content"

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

#What to show in extra content title
EXTRA_TITLE = 'Useful Links'

#Adds text
EXTRA_CONTENT = 'Test extra content'

#Sows a list of links
EXTRA_LINKS = (('Bot Commands', 'https://4s3ti.net/4gentsm1th-commands.html'),
                ('Link Shortener', 'https://s.4s3ti.net'),
                ('Pastebin', 'https://paste.4s3ti.net'),)



SIDEBAR_DISPLAY = ['about', 'categories', 'tags', 'extra', 'authors']
SIDEBAR_ABOUT = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi quae hic dicta eius ad quam eligendi minima praesentium voluptatum? Quidem quaerat eaque libero velit impedit dicta, repudiandae sapiente. Deserunt, excepturi."



# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True