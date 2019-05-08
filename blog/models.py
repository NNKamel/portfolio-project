from django.db import models

# Create your models here.
class Blog(models.Model):
    # title, pub_date, body, image
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField() #
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def summary(self):
        d = ["..."]
        if(len(self.body)>100):
            return self.body[:100]+ "..."
        else:
            return self.body

    def out_date(self):
        return self.pub_date.strftime('%d %B, %Y')
