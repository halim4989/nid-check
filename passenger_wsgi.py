#python 3.7.9
#SERVER DEPLOYMENT

import sys, os

INTERP = "<PATH TO PYTHON3 VIRTUAL ENV>/bin/python"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from nid_check import app as application