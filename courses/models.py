from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50,blank=False) #URLField()
    # slug = models.SlugField()
    date = models.DateField()
    isActive = models.BooleanField(default=True)
    # isUpdated = models.BooleanField(default=False)

    