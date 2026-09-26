import uuid
from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Service(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255, blank=True, null=True)
    starred_by = models.ManyToManyField(
        User, related_name="starred_services", blank=True
    )
    def __str__(self):
        return self.title