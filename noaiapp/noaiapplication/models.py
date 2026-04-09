from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
from django.db import models
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
