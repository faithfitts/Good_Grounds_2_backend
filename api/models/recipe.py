from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Recipe(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  description = models.TextField()
  method = models.TextField()
  ingredients = models.TextField()
  owner = models.ForeignKey(
      get_user_model(),
      # related_name='recipes',
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"{self.id}, {self.name}, {self.description}, {self.method}, {self.ingredients}"


  def as_dict(self):
    """Returns dictionary version of Recipe models"""
    return {
        'id': self.id,
        'description': self.description,
        'method': self.method,
        'ingredients': self.ingredients
    }
