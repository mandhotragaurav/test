from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ContacUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.IntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username