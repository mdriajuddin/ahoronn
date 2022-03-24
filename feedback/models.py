from django.db import models
from django.conf import settings
# Create your models here.
from catalog.models import Madicine

import uuid

class Feedback(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    feedback_content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)

    madicine = models.ForeignKey(Madicine, related_name='Madicine', on_delete=models.CASCADE)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.id)