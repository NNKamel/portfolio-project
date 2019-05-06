from django.db import models

# Create your models here.
class Blog(models.Model):
    # title, pub_date, body, image
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now=True) #
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
