from django.db import models


# Create your models here.
class DocumentType(models.Model):
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.description
