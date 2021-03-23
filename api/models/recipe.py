from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Recipe(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  method = models.CharField(max_length=100)
  ingredients = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The coffee creation named '{self.title}' would be described as {self.description}. It was created using this method {self.method} using these ingredients '{self.ingredients}'."

  def as_dict(self):
    """Returns dictionary version of Recipe models"""
    return {
        'id': self.id,
        'title': self.name,
        'description': self.ripe,
        'method': self.color,
        'ingredients': self.ingredients,
        'owner': self.owner
    }
