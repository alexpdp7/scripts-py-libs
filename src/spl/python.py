import os
import shutil

import spl
from spl import utils


@spl.register_command
def ensure_poetry(args):
    if shutil.which("poetry"):
        return
    assert os.environ.get(
        "SPL_BOOTSTRAP_POETRY_WITH_PIPX"
    ), "SPL_BOOTSTRAP_POETRY_WITH_PIPX not set, cannot bootstrap poetry"
    utils.run_command(["pipx", "install", "poetry"])
    utils.run_command(["poetry", "install"])


@spl.register_command
def format(args):
    run_black(args)


@spl.register_command
def run_black(args):
    ensure_poetry(args)
    utils.run_command(["poetry", "run", "black", "src"])


@spl.register_command
def validate(args):
    run_flake8(args)
    run_pytest(args)


@spl.register_command
def run_flake8(args):
    ensure_poetry(args)
    utils.run_command(["poetry", "run", "flake8", "src"])


@spl.register_command
def run_pytest(args):
    ensure_poetry(args)
    utils.run_command(["poetry", "run", "pytest"])
