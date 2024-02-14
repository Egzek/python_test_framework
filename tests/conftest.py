import pytest

from datetime import datetime
from pathlib import Path

headless_mode = ["true", "false"]


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        default="true",
        choices=sorted(headless_mode),
        help="Set to true if you want to run test on local browser in headless mode",
    )


# Creating log files for each test
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_setup(item):
    config = item.config
    logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
    filename = Path(
        "logs",
        f"{item._request.node.name}_{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.log",
    )
    logging_plugin.set_log_path(str(filename))
    yield
