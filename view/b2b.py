
from view.core import coreHandler


class b2bHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle=''
        )
        self.render('b2b.html', data=data)
