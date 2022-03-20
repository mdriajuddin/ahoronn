from django.db import models

# Create your models here.


class Pescription(models.Model):
    phone_number = models.CharField(max_length=11,null=True)



class Pescription_image(models.Model):
    image = models.ImageField(upload_to='pesceiption/', null=True)
    p_images = models.ForeignKey(Pescription, on_delete=models.CASCADE,)
