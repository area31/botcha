#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Guei(Base_Command.Base_Command):

    def guei(self):
        try:
            db = Database()
            xinga = db.select('xinga', 'xingamentos', 1)[0][0]
            user = db.select('guei', 'guei', 1)[0][0]
            self.parent.conn.privmsg(self.channel, '%s, %s' % (user, xinga))
        except:
            return False

    def run(self):
        self.guei()
