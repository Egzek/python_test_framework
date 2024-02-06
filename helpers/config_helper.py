import os
from dotenv import dotenv_values

from helpers.common import get_project_root as ROOT


def get_dotenv_config():
    APP_ENVIRONMENT = "qa" if not (env := os.environ.get("ENV")) else env
    env_path = ROOT() / "resources" / "envs"
    return dotenv_values(f"{env_path}/.env.{APP_ENVIRONMENT}")
