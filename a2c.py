import re
import sys
from subprocess import run
from urllib.parse import unquote_plus

link = sys.argv[1]

try:
  run(f'extra-api', -x 10 "{link}", shell=True)


print ('%s' % unquote_plus(link).rsplit('/', 1)[-1])
