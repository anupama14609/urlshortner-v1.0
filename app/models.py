from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=30)

    def __str__(self):
        return str(self.link)