import pytest

from datetime import datetime
from pathlib import Path


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
