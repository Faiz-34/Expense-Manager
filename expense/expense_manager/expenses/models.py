
from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=100, verbose_name="Expense title")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category=models.CharField(max_length=100,verbose_name="Expense category")


    def __str__(self):
        return str(self.id)
