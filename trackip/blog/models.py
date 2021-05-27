from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    author = models.CharField(max_length=50)
    def __str__(self):
        return self.title+' is posted by author '+self.author

# Create your models here.
