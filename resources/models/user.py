from dataclasses import dataclass


@dataclass
class User:
    password: str = None
    email: str = None


@dataclass
class UserCheckout:
    first_name: str = "test_first_name"
    last_name: str = "test_last_name"
    zip_code: str = "test_zip_code"
