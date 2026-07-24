from typing import TYPE_CHECKING

from django.db.models import QuerySet

from .notifications import Notification

if TYPE_CHECKING:
    from .models import Notification as NotificationModel


class Notifiable:
    """
    Inherited by a class that notifications can be sent to. e.g.
    a User class.
    """

    def notify(self, notification: Notification):
        """Send the notification to the notifiable."""
        delivery_channels = notification.via(self)

        for channel in delivery_channels:
            channel().send(notification=notification, notifiable=self)

    def notifications(self) -> QuerySet[NotificationModel]:
        """Return all notifications for the notifiable entity."""
        return self.notification_set.all()

    def unread_notifications(self) -> QuerySet[NotificationModel]:
        """Return all unread notifications for the notifiable entity."""
        return self.notification_set.unread()

    def read_notifications(self) -> QuerySet[NotificationModel]:
        """Return all unread notifications for the notifiable entity."""
        return self.notification_set.read()
