from django.db import models

# Create your models here.
class Counter(models.Model):
    count = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.date} : {self.count}'