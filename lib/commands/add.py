#  -*- coding: utf-8 -*-
#
from lib.commands import Base_Command
from lib.modules.database import Database

class Add(Base_Command.Base_Command):

    def admin(self, _nick):
        db = Database()
        try:
            db.insert('admins', _nick.strip())
        except:
            return False
        return True

    def quote(self, string):
        db = Database()
        try:
            db.insert('quotes', string.strip())
        except:
            return False
        return True

    def xingamento(self, string):
        db = Database()
        try:
            db.insert('xingamentos', string.strip())
        except:
            return False
        return True

    def noob(self, string):
        db = Database()
        try:
            db.insert('noob', string.strip())
        except:
            return False
        return True

    def ama(self, string):
        db = Database()
        try:
            db.insert('amoroso', string.strip())
        except:
            return False
        return True

    def chora(self, string):
        db = Database()
        try:
            db.insert('chora', string.strip())
        except:
            return False
        return True

    def mulher(self, string):
        db = Database()
        try:
            db.insert('mulheres', string.strip())
        except:
            return False
        return True

    def goatrance(self, string):
        db = Database()
        try:
            db.insert('goatrance', string.strip())
        except:
            return False
        return True

    def rock(self, string):
        db = Database()
        try:
            db.insert('rock', string.strip())
        except:
            return False
        return True

    def nerdices(self, string):
        db = Database()
        try:
            db.insert('nerdices', string.strip())
        except:
            return False
        return True

    def reggae(self, string):
        db = Database()
        try:
            db.insert('reggae', string.strip())
        except:
            return False
        return True

    def chill(self, string):
        db = Database()
        try:
            db.insert('chill', string.strip())
        except:
            return False
        return True

    def meme(self, string):
        db = Database()
        try:
            db.insert('meme', string.strip())
        except:
            return False
        return True

    def zuera(self, string):
        db = Database()
        try:
            db.insert('zuera', string.strip())
        except:
            return False
        return True

    def docs(self, string):
        db = Database()
        try:
            db.insert('docs', string.strip())
        except:
            return False
        return True

    def politica(self, string):
        db = Database()
        try:
            db.insert('politica', string.strip())
        except:
            return False
        return True

    def add(self):
        if len(self.args) > 1:
            content = ' '.join(self.args[1:])
            result = None
            if self.args[0] == 'admin' and self.check_admin():
                _db = Database()
                _nicks = [ nick[0] for nick in _db.select('admin', 'admins') ]
                if not content in _nicks:
                    result = self.admin(content)
                    if result:
                        self.parent.conn.privmsg(self.channel, "%s, %s adicionado." % (self.nick, self.args[0]))
                else:
                    self.parent.conn.privmsg(self.channel, "%s, este usuario ja eh admin." % (self.nick))

            if self.args[0] == 'quote':
                result = self.quote(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, %s adicionado." % (self.nick, self.args[0]))

            if self.args[0] == 'xingamento':
                result = self.xingamento(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, %s adicionado." % (self.nick, self.args[0]))

            if self.args[0] == 'noob':
                result = self.noob(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, fala de %s adicionada." % (self.nick, self.args[0]))

            if self.args[0] == 'ama':
                result = self.ama(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, %s adicionado." % (self.nick, self.args[0]))

            if self.args[0] == 'mulher':
                result = self.mulher(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, gostosa adicionada." % (self.nick))

            if self.args[0] == 'chora':
                result = self.chora(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, choro adicionado." % (self.nick))

            if self.args[0] == 'goatrance':
                result = self.goatrance(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, goa trance adicionado." % (self.nick))

            if self.args[0] == 'rock':
                result = self.rock(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, Rock (vulgo Roque) adicionado." % (self.nick))

            if self.args[0] == 'reggae':
                result = self.reggae(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, Som de maconheiro medicinal adicionado." % (self.nick))

            if self.args[0] == 'nerdices':
                result = self.nerdices(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, Nerdice adicionada seu virje." % (self.nick))

            if self.args[0] == 'chill':
                result = self.chill(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, Chillout adicionado." % (self.nick))

            if self.args[0] == 'meme':
                result = self.meme(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, Meme (ou mene) adicionado." % (self.nick))

            if self.args[0] == 'zuera':
                result = self.zuera(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, Zuera adicionada, SEU ZUERO." % (self.nick))

            if self.args[0] == 'docs':
                result = self.docs(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, Artigo adicionado." % (self.nick))

            if self.args[0] == 'politica':
                result = self.politica(content)
                if result:
                    self.parent.conn.privmsg(self.channel, "%s, Politica adicionada." % (self.nick))
	else:
		self.parent.conn.privmsg(self.channel, "%s, deixa de ser burro e adiciona alguma coisa direito." % self.nick)

    def run(self):
        self.add()
