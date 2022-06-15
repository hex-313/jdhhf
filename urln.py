import re
import sys
from urllib.parse import unquote_plus

print ('%s' % unquote_plus(sys.argv[1]).rsplit('/', 1)[-1])
