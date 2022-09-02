from django.db import models
class Twitte(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateField(auto_now=True)
    like = models.IntegerField(default=0,null=True,blank=True)