from dataclasses import dataclass


@dataclass
class User:
    password: str = None
    email: str = None
