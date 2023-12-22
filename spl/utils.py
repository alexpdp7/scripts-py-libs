import logging
import shlex
import subprocess


logger = logging.getLogger(__name__)


def run_command(command):
    logger.info("running %(command)s", {"command": shlex.join(command)})
    subprocess.run(command, check=True)
