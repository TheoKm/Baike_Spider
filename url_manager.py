class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
<<<<<<< HEAD
<<<<<<< HEAD
        return new_url
=======
        return new_url
>>>>>>> 3d10976de6f3354ea5b2d0c348dfa56e71834de6
=======
        return new_url
>>>>>>> 3d10976de6f3354ea5b2d0c348dfa56e71834de6
