import os

import nox
BASE = os.path.abspath(os.path.dirname(__file__))

DEFAULT_PYTHON_VERSIONS = ["/usr/bin/python3.8"]

PYTHON_VERSIONS = os.environ.get(
    "NOX_PYTHON_VERSIONS", ",".join(DEFAULT_PYTHON_VERSIONS)
).split(",")


def deps(session, editable_install):
    session.install('--upgrade', "setuptools", "pip")
    extra_flags = ["-e"] if editable_install else []
    session.install("-r", "requirements/requirements.txt", silent=False)

@nox.session(python=PYTHON_VERSIONS)
def pyalgo(session):
    deps(session, editable_install=True)
