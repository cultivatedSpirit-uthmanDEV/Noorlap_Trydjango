"""
To render html web pages

"""

HTML_STRING = """
  <h1>Hello world</h1>

"""
from django.http import HttpResponse

def home(request):
  """
   Take in a request (Django sends request)
   Return HTML as a response (We pick to return the response)
  """
  return HttpResponse(HTML_STRING)