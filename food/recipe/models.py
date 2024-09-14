from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)

    def __str__(self):
        return self.name
