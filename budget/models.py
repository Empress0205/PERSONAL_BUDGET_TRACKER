from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100)
    type = models.CharField(choices=TRANSACTION_TYPES, max_length=10)
    
    def get_balance(self):
        income = Transaction.objects.filter(user=self, type='income').aggregate(total=sum('amount'))['total'] or 0
        expense = Transaction.objects.filter(user=self, type='expense').aggregate(total=sum('amount'))['total'] or 0
        return income - expense
    
    def __str__(self):
        return f"{self.type.capitalize()} - {self.amount} - {self.date}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)  # Optional bio

    def __str__(self):
        return f"Profile of {self.user.username}"
    
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Expense by {self.user.username} on {self.date}"
