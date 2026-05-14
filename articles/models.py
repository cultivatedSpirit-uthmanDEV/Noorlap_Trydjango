from django.db import models
from django.utils import timezone

# Create your models here.
class Articles(models.Model):
  title = models.CharField(max_length=120)
  content = models.TextField() 
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True )
  publish = models.DateField(auto_now_add=False, auto_now=False, null=True)

  ## Django shell

##  obj2.save()
#>>> obj2.id 5
    #  >>> obj2
     # <Articles: Articles object (5)>
      #>>> a= Articles.objects.get(id=5)
      #>>> a.title
      #'this is cool'
      #>>> b = Articles.objects.get(id=4)
      #>>> b.title
      #'This is my other title'