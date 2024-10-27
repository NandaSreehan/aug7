from django.db import models
class lists(models.Model):
    uname=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now=True)
    post=models.CharField(max_length=400)
    def __str__(self):
        return self.uname

# Create your models here.
