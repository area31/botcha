#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Docs(Base_Command.Base_Command):

    def docs(self):
        db = Database()
        self.docs = None
        try:
            self.docs = db.select('docs', 'docs', 1)[0][0]
        except:
            return False
        if self.docs:
            self.parent.conn.privmsg(self.channel, self.docs)

    def run(self):
        self.docs()
