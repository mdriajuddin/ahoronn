from django.db import models

# Create your models here.


class Pescription(models.Model):
    phone_number = models.CharField(max_length=11,null=True)
    image = models.ImageField(upload_to='medicine/', null=True)
    def __str__(self):
        return self.phone_number
