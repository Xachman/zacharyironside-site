from flask import Markup

class Nav:
    def __init__(self, path = ""):
        self.path = path

    def makelink(self, path, name):
        active = False
        if path == self.path:
            active = True

        return Markup('<li class="'+('active' if active else '')+'"><a href="'+path+'">'+name+'</a></li>')