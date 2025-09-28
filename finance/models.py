from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Transaction(models.Model):
    Transaction_Types = [
        ('Income', 'Income'),
        ('Expense', 'Expense')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=Transaction_Types)
    date = models.DateField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

    def __str__(self):
        return self.name


