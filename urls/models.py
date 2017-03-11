from django.db import models
from django.conf import settings


class Url(models.Model):
    user     = models.ForeignKey(settings.AUTH_USER_MODEL)
    url      = models.TextField()
    code     = models.CharField(max_length=8)
    updated  = models.DateTimeField(auto_now=True)
    created  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class UrlAnalitys(models.Model):
    url     = models.ForeignKey(Url, related_name='analitys')
    browser  = models.CharField(max_length=255)
    os  = models.CharField(max_length=255)
    ip  = models.CharField(max_length=20)
    created  = models.DateTimeField(auto_now_add=True)
    
