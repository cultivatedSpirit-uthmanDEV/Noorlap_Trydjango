"""
To render html web pages

"""

import random
from django.http import HttpResponse

def home_view(request):
  """
   Take in a request (Django sends request)
   Return HTML as a response (We pick to return the response)
  """
  number = random.randint(10,200000)
  name = 'Uthman'
   #Django Template
  H1_string = f"""
  <h1>Hello {name} - {number}</h1>"""

  p_string = f"""
  <p>Hello {name} - {number}</p>"""

  HTML_STRING = H1_string + p_string
  

  print(1000 * 9)
  return HttpResponse(HTML_STRING)