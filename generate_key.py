#!/usr/bin/python2.6
#  -*- coding: utf-8 -*-
#
from lib.modules.database import Database
import os
import random
import string

debug = True

length = 48
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(8192))
_hash = ''.join(random.choice(chars) for i in range(length))

try:
    db = Database()
    db.update('crypto', 'hash', _hash)
    if debug:
        print "Generating crypto password: %s" % _hash
except Exception, e:
    print "Error: %s" % repr(e)
