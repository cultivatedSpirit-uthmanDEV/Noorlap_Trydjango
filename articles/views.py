from django.shortcuts import render

from .models import Articles
# Create your views here.

def articles_search_view(request):
    #print(dir(request))
    #print(request.GET)
    query_dict = request.GET # this is a dictionary
    #query = query_dict.get("q") #  <input type="text" name="q"/>

    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    article_obj = None
    if query is not None:
      article_obj = Articles.objects.get(id=query)
    context = {
        "object": article_obj
        }
    return render(request, "articles/search.html",context=context)

def articles_create_view(request):
  
    context = { }
    return render(request, "articles/create.html",context=context )

def articles_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Articles.objects.get(id=id)
    context = {
        "object": article_obj
    }
    return render(request, "articles/detail.html",context=context )