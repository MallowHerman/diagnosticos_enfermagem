from django.db import models

class Diagnoses(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
