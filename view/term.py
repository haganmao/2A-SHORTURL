from view.core import coreHandler


class termHandler(coreHandler):

    def get(self):
        self.render("term.html")

