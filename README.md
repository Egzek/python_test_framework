# Selenium Automation Testing

This is a simple selenium testing framework meant for [Python](https://www.python.org/downloads/) 3.12 and newer (not compatible with older versions).

I am using [SauceDemo](https://www.saucedemo.com/) as a testing site. It was created mainly for testing UI, but I am using it for testing **E2E**, which is a little bit different.

Several important things:
- Tests use the [Py.test](https://docs.pytest.org/en/latest/) framework as test runner.
- Repo is formatted with [black](https://github.com/psf/black).
- [flake8](https://flake8.pycqa.org/en/latest/) is used for styling correction.
- [Typing hints](https://docs.python.org/3/library/typing.html) are very useful for code clearance and error prune code.

## Usage
Clone the repo. Then use:

```bash
pip install -r requirements.txt
```

I have provided the `.env.qa` file but we can have several envs like `.env.prod, .env.stage` etc.

Note: normally .env file should **NOT** be kept in repo, but in some cloud service or other place.
Here, as it uses publicly available data and for demo purposes, it is kept in repo.


## Running tests
To run the tests you can use either pytest itself or tox. Sample commands:

```bash
tox file_name.py
pytest file_name.py
pytest -m sample_flag
```

On default, tests are launched on **qa** environment. We can change it to some other env adding ```ENV=sample_env``` flag before tox/pytest i.e:

`ENV=prod pytest -m login`


For each test we save logs which can be found in the log folder. If test fails, picture is taken automatically and can be found in results/screenshots folder.

