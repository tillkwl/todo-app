from django.db import models
from apps.core.models import TimestampedModel
from apps.users.models import AppUser

class Project(TimestampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name='created_projects',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name