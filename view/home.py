

from view.core import coreHandler




# Home handler
class HomeHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle="Try 2a Short Url Provider, You'll Like It"
        )
        self.render("home.html", data=data)

    def post(self):
        res = dict(code=0)
        form = urlForm(MultiDict(self.urlFormParams))
        if form.validate():
            res["code"] = 1
        else:
            res = form.errors
            res["code"] = 0
        self.write(res)
