from email.policy import default
from telnetlib import STATUS
from django.db import models

# Create your models here.

class Task(models.Model):

    STATUS = (
        ('Digital', 'Digital'),
        ('Physical', 'Physical'),
    )
    productname = models.CharField(max_length=200, null=True)
    producttype = models.CharField(max_length=200, null=True, choices=STATUS)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(default='xxx.jpg', null=True, blank=True  )

    def __str__(self):
        return self.productname


