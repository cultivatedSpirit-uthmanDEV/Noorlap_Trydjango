from django.db import models

# Create your models here.
class Articles(models.Model):
  title = models.TextField()
  content = models.TextField() 

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