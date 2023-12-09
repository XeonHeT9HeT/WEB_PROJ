from django.db import models

class Farma(models.Model):
    name = models.CharField(max_length=50)
    agent = models.CharField(max_length=50)
    form = models.CharField(max_length=10)
    action = models.CharField(max_length=500)
    need = models.CharField(max_length=500)
    non = models.CharField(max_length=500)
    subAction = models.CharField(max_length=500)
