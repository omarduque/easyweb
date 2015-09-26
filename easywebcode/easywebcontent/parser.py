__author__ = 'abeduarterey'
from StringIO import StringIO
import pycurl
import simplejson


class wikihow():

    @staticmethod
    def searchWikiHow(search_query):

        searchwikiurl = 'http://www.wikihow.com/api.php?action=query&list=search&srwhat=text&format=json&srprop=snippet|wordcount|sectionsnippet&srsearch='
        results = []
        if search_query == 'none':
            results.append('no key')
        else:
            query = searchwikiurl+search_query
            buffer = StringIO()
            connection = pycurl.Curl()
            connection.setopt(connection.URL, query)
            connection.setopt(connection.WRITEDATA, buffer)
            connection.perform()
            connection.close()
            results = simplejson.loads(buffer.getvalue())

        return results

    @staticmethod
    def searchWikiArticle(search_query):

        searchwikiurl = 'http://www.wikihow.com/api.php?action=app&subcmd=article&format=json&name='
        results = []
        if search_query == 'none':
            results.append('no key')
        else:
            query = searchwikiurl + search_query
            buffer = StringIO()
            connection = pycurl.Curl()
            connection.setopt(connection.URL, query)
            connection.setopt(connection.WRITEDATA, buffer)
            connection.perform()
            connection.close()
            results = simplejson.loads(buffer.getvalue())

        return results

    @staticmethod
    def extract_title(search_result):
        title = search_result['query']['search'][00]['title']
        return title

    @staticmethod
    def extract_snippet(search_result):
        snippet = search_result['query']['search'][00]['snippet']
        return snippet

    @staticmethod
    def extract_fulltitle(search_result):
        snippet = search_result['app']['fulltitle']
        return snippet

    @staticmethod
    def extract_abstract(search_result):
        snippet = search_result['app']['abstract']
        return snippet

    @staticmethod
    def extract_url(search_result):
        snippet = search_result['app']['url']
        return snippet

    @staticmethod
    def extract_image(search_result):
        snippet = search_result['app']['image']['original']
        return snippet

    @staticmethod
    def extract_sections(search_result):
        snippet = search_result['app']['sections'][00]
        return snippet




