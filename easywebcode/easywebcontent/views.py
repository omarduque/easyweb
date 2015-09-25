from django.shortcuts import render
# Create your views here.

def index(request):
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)
        # Do whatever you need with the word the user looked for
    return render(request, 'index.html')
    # Your code
