#debug
DEBUG = True
TEMPLATE_DEBUG = DEBUG

#database
DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'spills'
DATABASE_USER = 'root'
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

PROJECT_DIR = '/data/vhost/spills/spills'

# Absolute path to the directory that holds media.
MEDIA_ROOT = PROJECT_DIR + '/media'
ADMIN_MEDIA_ROOT = PROJECT_DIR + '/media'

# templates
TEMPLATE_DIRS = (
    PROJECT_DIR + "/templates"
)

#admins
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS