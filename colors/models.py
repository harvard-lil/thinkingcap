from django.db import models


class Color(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)