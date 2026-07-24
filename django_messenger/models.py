from django.contrib.auth import get_user_model
from django.db import models


class NotificationManager(models.Manager):
    def mark_as_read(self):
        return self.update(is_read=True)

    def unread(self):
        return self.filter(is_read=False)

    def read(self):
        return self.filter(is_read=False)


class Notification(models.Model):
    data = models.JSONField()
    is_read = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = NotificationManager
