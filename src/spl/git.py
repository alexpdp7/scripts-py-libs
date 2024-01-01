import pathlib

from spl import utils


def describe(long):
    long_args = ["--long"] if long else []
    description = utils.run_command(
        ["git", "describe", "--all", "--always"] + long_args, capture_stdout=True
    ).stdout
    assert description.startswith("heads/"), f"unexpected description {description}"
    return description[len("heads/") : -1]  # remove heads/ and trailing newline


def is_dirty():
    returncode = utils.run_command(
        ["git", "diff-index", "--quiet", "HEAD", "--"], check=False
    ).returncode
    assert returncode in (0, 1), f"returncode is {returncode}"
    return returncode == 1


def project_name():
    return pathlib.Path.cwd().name
