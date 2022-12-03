from django.db import models
from django.template.defaultfilters import slugify

class Diagnoses(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-")
        return super().save(*args, **kwargs)