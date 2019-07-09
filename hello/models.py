from django.db import models

# Create your models here.

class Newthing(models.Model):
    title = models.CharField(max_length= 100)
    pubdate = models.DateTimeField('date published')
    body = models.TextField()
    postit = models.IntegerField(default=0)

    def __str__(self):
     return self.title

    def hittingPoint(self):
         self.postit = self.postit +1
         self.save()