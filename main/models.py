from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Namaz(models.Model):    
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    code = models.IntegerField(unique=True)
    
    class Meta:
        ordering = ['code']
        verbose_name_plural = 'namaz'
        
    def __str__(self):
        return self.name
    
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    namaz = models.ForeignKey(Namaz, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'entries'
        
    def __str__(self):
        return f"{self.user.username} - {self.namaz.name}({self.quantity})"
    