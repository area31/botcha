#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Xinga(Base_Command.Base_Command):

    def xinga(self):
        if len(self.args) < 1:
            self.parent.conn.privmsg(self.channel,'%s, deixa de ser burro e xinga alguém direito. ' % self.nick)	
        else:
            db = Database()
            self.xinga = None
            try:
                self.xinga = db.select('xinga', 'xingamentos', 1)[0][0]
                if self.xinga:
                    self.parent.conn.privmsg(self.channel, '%s, %s' % (self.args[0].decode('utf-8').encode('utf-8'), self.xinga))
            except:
                return False

    def run(self):
        self.xinga()
