import logging
import os
from dotenv import dotenv_values

from helpers.common import get_project_root as ROOT
from helpers.singleton import Singleton
from resources.custom_errors.env_error import WrongEnviroment

logger = logging.getLogger()


class Config(metaclass=Singleton):
    _env_path = ROOT() / "resources" / "envs"
    _available_config = {"qa", "prod"}

    def __init__(self):
        env = os.environ.get("ENV")
        if env is None:
            env = "qa"
            os.environ["ENV"] = "qa"
        if env not in self._available_config:
            raise WrongEnviroment(env_specified=env, env_expected=self._available_config)
        logger.debug(f"Running against {env} env")
        self.env = dotenv_values(f"{self._env_path}/.env.{env}")

    def get_dotenv_config(self):
        return self.env
