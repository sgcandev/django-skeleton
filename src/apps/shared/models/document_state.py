from django.db import models


# Create your models here.
class DocumentState(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
