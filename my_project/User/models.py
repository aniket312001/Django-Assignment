
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth


# class User(models.Model):                              # it will just create redency so use default user table
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=245)
#     password = models.CharField(max_length=55)
#     username = models.CharField(max_length=30)

#     def __str__(self):
#         return self.username


class Post(models.Model):
    p_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=1000)
    text = models.CharField(max_length=500000)
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    update_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user.username