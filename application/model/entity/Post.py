from datetime import datetime
from application.model.dao import postDAO


class Post:
    def __init__(self, name, text):
        self._id = len(postDAO.list_post()) + 1
        self._name = name
        self._text = text
        self._created_date = datetime.now().strftime('%d/%m/%Y')

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def date(self):
        return self._created_date
