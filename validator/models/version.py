from django.db import models


class DatasetVersion(models.Model):
    short_name = models.CharField(max_length=30)
    pretty_name = models.CharField(max_length=30)
    help_text = models.CharField(max_length=150)

    def __str__(self):
        return self.short_name
