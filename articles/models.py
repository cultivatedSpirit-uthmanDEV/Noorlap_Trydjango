from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Articles(models.Model):
      title = models.CharField(max_length=120)
      slug = models.SlugField(blank=True, null=True)
      content = models.TextField() 
      timestamp = models.DateTimeField(auto_now_add=True)
      updated = models.DateTimeField(auto_now=True )
      publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)


        
      """def save(self, *args, **kwargs):
            if self.slug is None:
              self.slug = slugify(self.title)
            super().save(*args, **kwargs)"""
      
      
def article_pre_save(sender, instance, *args, **kwargs):
           #print('pre_save')
          if instance.slug is None:
             instance.slug = slugify(instance.title)

pre_save.connect(article_pre_save, sender=Articles)


def article_post_save(sender, instance, created, *args, **kwargs):
           #print('post_save')
     if created:
          instance.slug = "this is my slug"
          instance.save()

               
post_save.connect(article_post_save, sender=Articles)
      










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