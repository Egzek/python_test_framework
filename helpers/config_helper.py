import logging
import os
from dotenv import dotenv_values

from helpers.common import get_project_root as ROOT
from helpers.singleton import Singleton

logger = logging.getLogger()


class Config(metaclass=Singleton):
    _env_path = ROOT() / "resources" / "envs"
    _available_config = {"qa", "prod"}

    def __init__(self):
        app_env = "qa" if not (env := os.environ.get("ENV")) else env
        if app_env not in self._available_config:
            raise EnvironmentError
        logger.info(f"Running against {app_env} env")
        self.env = dotenv_values(f"{self._env_path}/.env.{app_env}")

    def get_dotenv_config(self):
        return self.env
