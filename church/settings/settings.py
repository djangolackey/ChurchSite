# Django settings for homesite project.
from churchsecret import *

import sys
sys.path.remove('/home/jlindsey/webapps/hmdjango/lib/python2.5')
sys.path.insert(0, '/home/jlindsey/webapps/hmdjango/church/apps/Django-1.2.1')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jeff Lindsey', 'jeff@jlindseyfamily.net'),
    ('Jeff Lindsey', 'jlindsey@arkansasonline.com'),
)

MANAGERS = ADMINS

SIGNAL_EMAILS = ('jeff@jlindseyfamily.net')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/jlindsey/webapps/media/church/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/church/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/church_admin_media/'

# Defaults to MEDIA_URL + 'snapboard/'
#SNAP_MEDIA_PREFIX = '/media/snapboard/media'

# Set to False if your templates include the SNAPboard login form
#USE_SNAPBOARD_LOGIN_FORM = True

# Select your filter, the default is Markdown
# Possible values: 'bbcode', 'markdown', 'textile'
#SNAP_POST_FILTER = 'bbcode'

# This is the number of days a person has to register there account after submitting the registration form
ACCOUNT_ACTIVATION_DAYS = 14

#Force all tags to be lowercase
FORCE_LOWERCASE_TAGS = True

# Sending email from Django settings
EMAIL_HOST='smtp.webfaction.com'
EMAIL_PORT='25'
DEFAULT_FROM_EMAIL = "djangoserver@jlindseyfamily.net"
SERVER_EMAIL = "djangoserver@jlindseyfamily.net"

CACHE_BACKEND = 'memcached://unix:/home/jlindsey/memcached.sock'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'church.settings.loginrequired.EnforceLoginMiddleware',
#    'homesite.FacebookConnectMiddleware.FacebookConnectMiddleware',
#    'django.middleware.loginrequired.EnforceLoginMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
#    'snapboard.middleware.threadlocals.ThreadLocals',

    # These are optional
#    'snapboard.middleware.ban.IPBanMiddleware',
#    'snapboard.middleware.ban.UserBanMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
#    'snapboard.views.snapboard_default_context',
)

AUTH_PROFILE_MODULE = 'profiles.profile'

LOGIN_REDIRECT_URL = '/accounts/login/'

PUBLIC_URLS = (
    r'admin/',
    r'books/.*',
    r'info/.*',
    r'accounts/login/',
    r'$',
    r'accounts/register/',
    r'accounts/password/reset/',
    r'pastors-pen/.*',
    r'sermons/.*',
    r'links/.*',
)

SERVE_STATIC_TO_PUBLIC = True

ROOT_URLCONF = 'urls'

TEMPLATE_ROOT = '/home/jlindsey/webapps/hmdjango/church'
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    r'%s/homesite/site_%d_templates' % (TEMPLATE_ROOT, SITE_ID),
    r'%s/templates' % TEMPLATE_ROOT,
#    r'%s/homesite/church/templates/basic' % TEMPLATE_ROOT,
#    r'%s/homesite/common/accounts/templates' % TEMPLATE_ROOT,
    r'/home/jlindsey/webapps/hmdjango/church/apps/Django-1.2.1/django/contrib/admin/templates',
)



INSTALLED_APPS = (
#    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.redirects',
    'tagging',
#    'diario',
    'basic.*',
#    'pagination',
    'notification',
    'mailer',
#    'mailer',
#    'snapboard',
#    'jellyroll',
    'treemenus',
    'menu_extension',
    'registration',
    'documents',
    'photologue',
    'churchmembers',
#    'tumblelog',
)
