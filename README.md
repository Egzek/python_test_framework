# Selenium Automation Testing

This is a simple selenium testing framework meant for [Python](https://www.python.org/downloads/) 3.12 and newer (not compatible with older versions).

I am using [SauceDemo](https://www.saucedemo.com/) as a testing site. It was created mainly for testing UI, but I am using it for testing **E2E**, which is a little bit different.

Several important things:
- Tests use the [Py.test](https://docs.pytest.org/en/latest/) framework as test runner.
- Repo is formatted with [black](https://github.com/psf/black).
- [flake8](https://flake8.pycqa.org/en/latest/) is used for styling correction.
- [Typing hints](https://docs.python.org/3/library/typing.html) are very useful for code clearance and error prune code.

## Installation
Clone the repo. Then use:

```bash
pip install -r requirements.txt
```


#### Pre-commit

This repo is using pre-commit to check code analysis with [black](https://github.com/psf/black) and [flake8](https://flake8.pycqa.org/en/latest/).
In order to run validation before each commit, use:

```bash
pre-commit install
```
This will add pre-commit to git hooks and perform the checks defined in `.pre-commit-config.yaml`

Note: every Merge Request must pass code analysis to merge it.

## Setting environment

On default, tests are launched on **qa** environment. We can change it to some other ENV adding ```ENV=sample_env``` flag before run command i.e:

`ENV=prod pytest -m login`

I have provided the `.env.qa` file. We can have several ENV files like `.env.prod,` `.env.stage` etc.

Note: normally .env file should **NOT** be kept in repo, but in protected cloud service or some other place.
Here, as it uses publicly available data and for demo purposes, it is kept in repo.


## Running tests
To run the tests, you can use either pytest or tox.

#### Running all tests

To run all the scripts, type:
```bash
pytest . 
```
#### Running specific test

```bash
pytest tests/front/test_login.py
```

You can also use specific flag:

```bash
pytest -m login
```

#### Tox

Tests can be run using tox, which creates a virtual env with all dependencies installed for every run:

```bash
tox -- front/test_login.py
```

## Results/Logs

For each test we save logs which can be found in the log folder. If the test fails, a picture is taken automatically and can be found in results/screenshots folder.

## GitHub Actions

This repo is using GitHub actions to check and validate each Merge Request:

1. Confirm the code analysis is passing.
2. Check if all tests are passing.