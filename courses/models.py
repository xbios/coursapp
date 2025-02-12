from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    imageUrl = models.URLField()
    slug = models.SlugField()
    date = models.DateField()
    isActive = models.BooleanField(default=True)
    isUpdated = models.BooleanField(default=False)

    