from django.db import models
from django.conf import settings

User_model = settings.AUTH_USER_MODEL


class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    owner = models.ForeignKey(
        User_model, related_name="meal", on_delete=models.CASCADE, null=True
    )
    recipes = models.ManyToManyField(
        "recipes.Recipe", related_name="meal_plans"
    )

    def __str__(self):
        return self.name
