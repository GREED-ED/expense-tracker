from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    def __str__(self):
        return self.title
        
