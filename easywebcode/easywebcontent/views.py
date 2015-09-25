from django.shortcuts import render
from parser import parser_wikihow
# Create your views here.

def index(request):
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)
        parser_wikihow.parse_wikihow_data()
        # the following are lines for implementing parsing
    return render(request, 'index.html')
    # Your code

