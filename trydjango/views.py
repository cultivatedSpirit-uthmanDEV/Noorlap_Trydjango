"""
To render html web pages

"""

import random
from django.http import HttpResponse

from django.template.loader import render_to_string
from articles.models import Articles


def articles_home_view(request):
  return HttpResponse



def home_view(request, id, *args, **kwargs):
  """
   Take in a request (Django sends request)
   Return HTML as a response (We pick to return the response)
  """

  print(args, kwargs)
  random_number = random.randint(1,4) # pseudocode
  name = 'Uthman' # hardcode

   ## from the database

  article_obj = Articles.objects.get(id = random_number)
  article_content = article_obj.content
  article_title = article_obj.title
  article_list = Articles.objects.all()
  Query_set = article_list #[103,105,108,290]



   

  context = {
    "Query_set" : article_list,
    "title": article_obj.title, 
    "content": article_obj.content,
    "id" : article_obj.id

  }
   #Django Template

   
  #tmpl = get_template("home-view.html")
  # tmpl_string = tmpl.render(context=context)

 
  

  H1_string = render_to_string("home-view.html",context = context)

  #H1_string = """  
  #<h1>Hello {title} - {content} 
  #( id:{id})!</h1>
  #<p>{content}</p>""".format(**context)

  

  print(1000 * 9)
  return HttpResponse(H1_string)