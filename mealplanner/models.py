from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    recipe_url = models.URLField()

    def __str__(self):
        return self.name
