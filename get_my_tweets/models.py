from django.db import models


class username(models.Model):
    username = models.CharField(max_length=100, primary_key=False)

