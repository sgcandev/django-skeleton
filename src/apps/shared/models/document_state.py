from django.db import models

from src.apps.core.models import CoreModel


# Create your models here.
class DocumentState(CoreModel):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
