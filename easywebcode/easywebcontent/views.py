from django.shortcuts import render
from parser import wikihow


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



