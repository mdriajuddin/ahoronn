from django.db import models

from django.conf import settings
from django.urls import reverse



import uuid

class Category(models.Model):
    category_title = models.CharField(max_length=20)


class Generic_name(models.Model):
    generic_name = models.CharField(max_length=50)


class Madicine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    trade_name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='medicine/', null=True)
    price = models.FloatField(null=True,blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True)
    generic_name = models.ForeignKey(Generic_name,on_delete=models.CASCADE ,null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.trade_name

    def get_absolute_url(self):
        return reverse('catalog:madicine_details',kwargs={'pk': self.id})

    def get_add_to_cart_url(self):
        return reverse('order:add-to-cart', kwargs={'pk': self.id})

    def get_remove_from_cart_url(self):
        return reverse("order:remove-from-cart",kwargs={'pk': self.id})
