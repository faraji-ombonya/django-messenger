from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .channels import Channel
    from .traits import Notifiable


class Notification(ABC):
    """
    The concrete class that inherits from this class should override
    the `via` method  and define other relevant message
    building methods, e.g `to_mail`, `to_database`, `to_sms`.
    """

    @abstractmethod
    def via(self, notifiable: Notifiable) -> list[Channel]:
        """Return a list of delivery channels.

        Determines which delivery channels the notification will be
        delivered to.
        """
        return []

    def database_type(self, notifiable: Notifiable):
        pass

    def initial_database_read_at_value(self):
        pass

    def mark_as_read(self):
        pass
