from view.core import coreHandler


class policylHandler(coreHandler):

    def get(self):
        self.render("policy.html")
