

from view.core import coreHandler
from view.core import urlForm,MultiDict



# Home handler
class HomeHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle="Try 2a Short Url Provider, You'll Like It"
        )
        self.render("home.html", data=data)

    
    def post(self):
        result = dict(res=0)
        urlform = urlForm(MultiDict(self.getFormData))
        if urlform.validate():
            result['res'] = 200
        else:
            result = urlform.errors
            result['res'] = 0
        self.write(result)

  