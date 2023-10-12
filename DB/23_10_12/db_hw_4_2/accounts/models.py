from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자 목록'