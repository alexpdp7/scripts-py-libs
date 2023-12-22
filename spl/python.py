import spl
from spl import utils


@spl.register_command
def format(args):
    run_black(args)


@spl.register_command
def run_black(args):
    utils.run_command(["black", "."])


@spl.register_command
def validate(args):
    run_flake8(args)


@spl.register_command
def run_flake8(args):
    utils.run_command(["flake8"])
