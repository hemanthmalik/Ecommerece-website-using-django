from django.db import models

# Create your models here.
class Feed(models.Model):
    feed_id = models.AutoField
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=600)
    pub_date = models.DateField()
    imageContent = models.ImageField(upload_to="blog/images")

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200)
    writer = models.CharField(max_length=50)
    intro = models.TextField()
    heading = models.CharField(max_length=100)
    headingcont = models.TextField(max_length=400)
    subheading = models.CharField(max_length=400)
    subcont = models.TextField(max_length=1500)

    def __str__(self):
        return self.writer
