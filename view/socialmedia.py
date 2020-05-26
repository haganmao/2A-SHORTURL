
from view.core import coreHandler


class socialmediaHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle=''
        )
        self.render('socialmedia.html', data=data)
