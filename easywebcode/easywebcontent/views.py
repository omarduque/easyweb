from django.shortcuts import render
from parser import wikihow
from StringIO import StringIO
import pycurl, simplejson
from models import Curated

# Create your views here.

def index(request):
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', 'none')
        if search_query is not 'none':
            results = wikihow.searchWikiHow(search_query)
            title = wikihow.extract_title(results)
            article_result = wikihow.searchWikiArticle(title)
            fulltitle = wikihow.extract_fulltitle(article_result)
            abstract = wikihow.extract_abstract(article_result)
            url = wikihow.extract_url(article_result)
            image = wikihow.extract_image(article_result)
            print (fulltitle)
            print (abstract)
            print (url)
            print (image)



    return render(request, 'index.html')
    # Your code



def displaycurated(request):
    if request.method == 'GET': # If the form is submitted
        title_id = request.GET.get('id', 'none')
        print title_id
        if title_id:
            article = Curated.objects.get(pk=title_id)
            fulltitle = article.title
            abstract = article.category+' '+article.name
            url=article.tool_url
            original = 'http://images.travelpod.com/tripwow/photos/ta-00b2-c3e0-0697/feel-the-beauty-of-nature-tibet-tibet+1152_12917392063-tpfil02aw-1676.jpg'

    return render(request, 
                    'results.html', 
                    {"fulltitle": article.title,
                     "abstract":article.abstract, 
                     "url":article.tool_url,
                     "original":original,
                     "html":article.html
                     }
                  )


