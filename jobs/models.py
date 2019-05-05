from django.db import models

class Job(models.Model): # models.Model links the class to the database
    image = models.ImageField(upload_to='images/')
    image_description = models.CharField(max_length=200)
