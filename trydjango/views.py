"""
To render html web pages

"""

import random
from django.http import HttpResponse


from articles.models import Articles



def home_view(request):
  """
   Take in a request (Django sends request)
   Return HTML as a response (We pick to return the response)
  """
  random_number = random.randint(1,4) # pseudocode
  name = 'Uthman' # hardcode

   ## from the database

  article_obj = Articles.objects.get(id = random_number)
  article_content = article_obj.content
  article_title = article_obj.title



   #Django Template
  H1_string = f"""
  <h1>Hello {article_title} - {article_content} ( id:{ article_obj.id})!</h1>"""

  p_string = f"""
  <p>Hello {name} - {random_number}</p>"""

  HTML_STRING = H1_string + p_string
  

  print(1000 * 9)
  return HttpResponse(HTML_STRING)