#  -*- coding: utf-8 -*-
#
import os, random, string

length = 48
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(8192))
print ''.join(random.choice(chars) for i in range(length))
