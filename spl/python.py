import subprocess

import spl


@spl.register_command
def format(args):
    run_black(args)


@spl.register_command
def run_black(args):
    subprocess.run(["black", "."], check=True)
