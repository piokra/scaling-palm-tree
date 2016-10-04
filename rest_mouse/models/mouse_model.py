from django.db import models


class MouseModel(models.Model):
    method = models.TextField(max_length=32)
    x = models.FloatField(blank=True)
    y = models.FloatField(blank=True)
