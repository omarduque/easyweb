__author__ = 'abeduarterey'
from StringIO import StringIO
import pycurl
import simplejson
import urllib

class wikihow():

    @staticmethod
    def searchWikiHow(search_query):

        searchwikiurl = 'http://www.wikihow.com/api.php?action=query&list=search&srwhat=text&format=json&srprop=snippet|wordcount|sectionsnippet&srsearch='
        results = []
        if search_query == 'none':
            results.append('no key')
        else:
            query = searchwikiurl + urllib.quote_plus(search_query)
            buffer = StringIO()
            connection = pycurl.Curl()
            connection.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')
            connection.setopt(connection.URL, query)
            connection.setopt(connection.WRITEDATA, buffer)
            connection.perform()
            connection.close()
            results = simplejson.loads(buffer.getvalue())

            # output = urllib2.urlopen(query).read()
            # results = simplejson.loads(output)

        return results

    @staticmethod
    def searchWikiArticle(search_query):

        searchwikiurl = 'http://www.wikihow.com/api.php?action=app&subcmd=article&format=json&name='
        results = []
        if search_query == 'none':
            results.append('no key')
        else:
            query = searchwikiurl + urllib.quote_plus(search_query)
            buffer = StringIO()
            connection = pycurl.Curl()
            connection.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')
            connection.setopt(connection.URL, query)
            connection.setopt(connection.WRITEDATA, buffer)
            connection.perform()
            connection.close()
            results = simplejson.loads(buffer.getvalue())

        return results

    @staticmethod
    def extract_title(search_result):
        result = search_result['query']['search'][00]['title']
        return result

    @staticmethod
    def extract_snippet(search_result):
        result = search_result['query']['search'][00]['snippet']
        return result

    @staticmethod
    def extract_fulltitle(search_result):
        result = search_result['app']['fulltitle']
        return result

    @staticmethod
    def extract_abstract(search_result):
        result = search_result['app']['abstract']
        return result

    @staticmethod
    def extract_url(search_result):
        result = search_result['app']['url']
        return result

    @staticmethod
    def extract_image(search_result):
        result = search_result['app']['image']['url']
        return result

    @staticmethod
    def extract_sections(search_result):
        result = search_result['app']['sections'][00]
        return result




