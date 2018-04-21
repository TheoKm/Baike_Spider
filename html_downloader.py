import urllib.request
import ssl
ssl._create_default_https_context =ssl._create_unverified_context
#After python 2.7.x,getting a https url must test and verify ssl
#import ssl,to disable the varification

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
