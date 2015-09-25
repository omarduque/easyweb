from django.shortcuts import render
from StringIO import StringIO
import pycurl, simplejson
# Create your views here.

def index(request):
    if request.method == 'GET': # If the form is submitted
    	search_query = request.GET.get('search_box', 'none')
        # Do whatever you need with the word the user looked for
        results = searchWikiHow(search_query)
        print (results)

    return render(request, 'index.html')
    # Your code

def searchWikiHow(search_query):
	searchwikiURL = 'http://www.wikihow.com/api.php?action=query&list=search&srwhat=text&format=json&srprop=snippet|wordcount|sectionsnippet&srsearch='
	results = []
	if search_query == 'none':
		results.append('no key') 
	else :
		query = searchwikiURL+search_query
	
		buffer = StringIO()
		connection = pycurl.Curl()
		connection.setopt(connection.URL, query)
		connection.setopt(connection.WRITEDATA, buffer)
		connection.perform()
		connection.close()
		
		results= simplejson.loads(buffer.getvalue())

	return results