from typing import Final

__all__ = [
    "NTFYUser"
]

class NTFYUser():
    """
    Attributes
    ----------
    username: :class:`str`
        user's username
    password: :class:`str`
        user's password
    """
    def __init__(self, username: str=None, password: str=None, token: str=None):
        self.username: Final[str] = username
        self.password: Final[str] = password
        self.token: Final[str] = token
    
    def auth(self) -> str:
        """
        Returns a ``username:password`` string
        """
        if self.username and self.password:
            return f"{self.username}:{self.password}"
        elif self.token:
            return self.token
        return ""
