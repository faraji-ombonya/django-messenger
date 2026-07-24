from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .channels import Channel
    from .notifications import Notification


class BaseRoute(ABC):

    def get_routes(self) -> list[tuple[Channel, str]]:
        return getattr(self, "routes", [])

    def notify(self, notification: Notification):
        """Send a notification to all the route entries."""

        for channel, address in self.get_routes():
            channel().send(notification=notification, address=address)


class Route(BaseRoute):
    def __init__(self, channel: Channel, address: str):
        self.routes = [(channel, address)]

    def route(self, channel: Channel, address: str):
        """Add a route to the list of routes and return self for chaining."""
        self.routes.append((channel, address))
        return self


class Routes(BaseRoute):
    def __init__(self, routes: list[tuple[str, str]]):
        self.routes = routes
