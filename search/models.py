from django.db import models

# Create your models here.


class Search(models.Model):
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.keyword