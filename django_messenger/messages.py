from abc import ABC


class Message(ABC):
    """Abstract message builder class.
    
    A class of this type can be returned by a message building 
    """

    def get_message(self):
        return getattr(self, "message", None)
