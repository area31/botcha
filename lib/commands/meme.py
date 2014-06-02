#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Meme(Base_Command.Base_Command):

    def meme(self):
        db = Database()
        self.meme = None
        try:
            self.meme = db.select('meme', 'meme', 1)[0][0]
        except:
            return False
        if self.meme:
            self.parent.conn.privmsg(self.channel, self.meme)

    def run(self):
        self.meme()
