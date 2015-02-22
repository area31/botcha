#  -*- coding: utf-8 -*-
#
from lib.modules.web import Web
import re

def ipinfo(args):
    try:
        web = Web()
        uri = 'http://whatismyipaddress.com/ip/'
        answer = web.html(web.get(uri + args))
        return answer

        th = answer.findAll('th')
        td = answer.findAll('td')

        infos = []
        for x in range(len(td)):
            key = th[x].string.lower().strip()
            value = re.sub('\([^()]+\)', '', re.sub('<[^<>]*>', '', str(td[x])).strip('\n').replace('&nbsp;', '').strip())
            if not value.startswith('None') and len(value):
                infos.append("%s %s" % (key, value))
        return ', '.join(infos)
    except Exception, e:
        return repr(e)

print ipinfo('8.8.8.8')
