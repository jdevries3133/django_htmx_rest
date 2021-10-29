Any and all contributors are welcome! We will be kind to one another and follow
the [Contributor's Covenant.](https://www.contributor-covenant.org/version/2/1/code_of_conduct/)

I am a relative novice developer who's been making software for only about two
years, so please be vocal if you know better than I do, because you very well
might!

# Project Setup

There is a minimal Makefile for setting up the environment and running tests.

### Makefile Security

All Makefile rules depend on venv creation, so any command may cause the
download and execution of project dependencies from PyPi. Proceed at your
discretion!

### Makefile Commands

If you wish you use it:

| command                | action                                                         |
| ---------------------- | -------------------------------------------------------------- |
| `make`                 | create virtual environment, and build package for distribution |
| `make test`            | run unit tests with pytest                                     |
| `make tox`             | run unit tests across version matrix with tox                  |
| `make pre-commit`      | run tests and format source code with black                    |
| `make dist-test`       | upload package to test-PyPi                                    |
| `make dist-production` | upload package to PyPi                                         |

## Workflow Without Makefile

Install dependencies and run tests like any Python/pytest project:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

pytest  # no additional args required
```

Before committing, be sure to format source code:

```
pytest && black src && echo "Good to go! 🙂"
```
