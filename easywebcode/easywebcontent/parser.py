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
    def extract_html(search_result):

        num_sections = len(search_result['app']['sections'])

        result = ''

        for x in range(0, num_sections - 1):

            type = search_result['app']['sections'][x]['type']

            if type == 'intro':

                testing = ''
                try:
                    value = search_result['app']['sections'][x]['image']['url']
                except KeyError:
                    testing = 'nokey'
                    pass

                if testing is not 'nokey':
                    result = result + search_result['app']['sections'][x]['image']['url']

                result = result + '</br>'
                result = result + search_result['app']['sections'][x]['html']
                result = result + '</br>'

            if type == 'steps':
                len_steps = len(search_result['app']['sections'][x]['methods'][0]['steps'])

                for y in range(0, len_steps - 1):

                    testing = ''
                    try:
                        value = search_result['app']['sections'][x]['image']['url']
                    except KeyError:
                        testing = 'nokey'
                    pass

                    result = result + '</br>'
                    result = result + '<h2>Step ' + search_result['app']['sections'][x]['methods'][0]['steps'][y]['num'] + '</h2>'

                    if testing is not 'nokey':
                        result = result + '<img src=' + search_result['app']['sections'][x]['methods'][0]['steps'][y]['image']['url'] + '>'

                    result = result + '</br>'
                    result = result + search_result['app']['sections'][x]['methods'][0]['steps'][y]['html']
                    result = result + '</br>'

        return result




