from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .notifications import Notification
    from .traits import Notifiable


class Channel(ABC):
    """
    Abstract base class that defines the blueprint of a delivery
    channel.

    Inherited by a concrete class that impelements exactly how
    the notification is sent to the
    """

    @abstractmethod
    def send(
        self,
        notification: Notification,
        notifiable: Notifiable | None = None,
        address: str | None = None,
    ):
        """
        Define how you want to send the notification to the
        notifiable or the address.
        """
        pass
