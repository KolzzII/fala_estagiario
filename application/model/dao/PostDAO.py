class PostDAO:
    def __init__(self):
        self._list_post = []

    def list_post(self):
        return self._list_post
        
    def insert_post(self, post):
        self._list_post.append(post)
