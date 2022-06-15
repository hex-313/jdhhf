import re
from urllib.parse import unquote_plus

link = ''

print ('%s' % unquote_plus(link).rsplit('/', 1)[-1])
