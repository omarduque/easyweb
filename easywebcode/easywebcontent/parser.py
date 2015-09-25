__author__ = 'abeduarterey'
import urllib2


class parser_wikihow():

    @staticmethod
    def parse_wikihow_data():
        data = urllib2.urlopen("http://www.wikihow.com/api.php?action=query&list=search&srwhat=text&format=json&srprop=snippet%7Cwordcount%7Csectionsnippet&srsearch=watch%20movie%20online").read()
        data = data.split('\n')