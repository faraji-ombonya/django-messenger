from .routes import Route, Routes
from .notifications import Notification as N
from .traits import Notifiable


class Notification(object):
    """Notification facade."""

    @classmethod
    def send(cls, notifiables: list[Notifiable], notification: N):
        """
        Sends the notification to the notifiables synchronously,
        using queues etc.
        """
        for n in notifiables:
            # TODO: send asynchronously.
            n.notify(notification)

    @classmethod
    def send_now(cls, notifiables: list[Notifiable], notification: N):
        """Sends the notification to the notifiables synchronously."""
        for n in notifiables:
            n.notify(notification)

    @classmethod
    def route(cls, channel, address):
        """
        Send an notification on demand.

        email, email_address
        sms, phone_number
        """
        return Route(channel, address)

    @classmethod
    def routes(cls, routes: list[tuple[str, str]]):
        """
        Send a notification on demand.
        [
            (email, email_address),
            (sms, phone_number),
        ]
        """
        return Routes(routes)
