from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class WebSite(models.Model):

  name = models.CharField(max_length=100)
  slug = models.SlugField(editable=False)
  url = models.URLField()
  description = models.CharField(max_length=100)
  designer = models.CharField(max_length=100)
  designer_url = models.URLField()
  twitter = models.CharField(max_length=50)
  image1 = models.ImageField(upload_to = 'websites')
  image2 = models.ImageField(upload_to = 'websites')
  image3 = models.ImageField(upload_to = 'websites', null=True, blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(WebSite, self).save(*args, **kwargs)

  def __str__(self):
    return self.name

class Vote(models.Model):

   user = models.ForeignKey(User, on_delete=models.CASCADE)
   website = models.ForeignKey(WebSite, on_delete
    =models.CASCADE)
   design = models.IntegerField()
   usability = models.IntegerField()
   creativity  = models.IntegerField()
   content  = models.IntegerField()

   def __str__(self):
     return "%s - %s" % (self.user.username, self.website.name)
     
