class WrongEnviroment(Exception):
    def __init__(self, env_specified: str, env_expected: set) -> None:
        self.message = f"Wrong env specified. We got {env_specified} but expected: {env_expected}"
        super().__init__(self.message)
