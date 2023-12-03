import tempfile
from typing import Any

import os

import nox
from nox.sessions import Session

package = "advent_of_code_2023"


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    """Install packages constrained by Poetry's lock file.

    This function is a wrapper for nox.sessions.Session.install. It
    invokes pip to install packages inside of the session's virtualenv.
    Additionally, pip is passed a constraints file generated from
    Poetry's lock file, to ensure that the packages are pinned to the
    versions specified in poetry.lock. This allows you to manage the
    packages as Poetry development dependencies.

    Arguments:
        session: The Session object.
        args: Command-line arguments for pip.
        kwargs: Additional keyword arguments for Session.install.

    """
    requirements = tempfile.NamedTemporaryFile(delete=False).name
    session.run(
        "poetry",
        "export",
        "--dev",
        "--format=requirements.txt",
        f"--output={requirements}",
        external=True,
    )
    session.install(f"--constraint={requirements}", *args, **kwargs)
    os.remove(requirements)

@nox.session(python=["3.12"])
def tests(session):
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, "pytest")
    session.run('pytest')