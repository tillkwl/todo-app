from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('member', 'Team Member'),
            ('leader', 'Team Leader'),
            ('admin', 'Administrator')
        ],
        default='member'
    )
    timezone = models.CharField(max_length=50, default='UTC')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'