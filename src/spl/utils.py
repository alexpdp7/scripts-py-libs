import logging
import shlex
import subprocess


logger = logging.getLogger(__name__)


def run_command(command, check=True, capture_stdout=False):
    logger.info("running %(command)s", {"command": shlex.join(command)})
    kwargs = {}
    if capture_stdout:
        kwargs["stdout"] = subprocess.PIPE
    return subprocess.run(command, check=check, encoding="utf8", **kwargs)
