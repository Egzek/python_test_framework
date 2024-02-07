from helpers.config_helper import get_dotenv_config


class Credentials:
    credentials = get_dotenv_config()
    default_user_mail = credentials.get("USERNAME_FOR_USER_DEFAULT")
    default_user_password = credentials.get("PASSWORD_FOR_USER_DEFAULT")
