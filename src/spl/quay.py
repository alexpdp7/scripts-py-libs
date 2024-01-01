import re

import spl
from spl import git, utils


QUAY_ORG = None


@spl.register_command
def build_images_and_push(args):
    tags = ["dirty"] if git.is_dirty() else [git.describe(False), git.describe(True)]
    for tag in tags:
        tag = re.sub(r"\W", "_", tag)
        quay_expires_after = "never" if not git.is_dirty() and tag == "main" else "3d"
        utils.run_command(
            [
                "podman",
                "build",
                ".",
                "--build-arg",
                f"QUAY_EXPIRES_AFTER={quay_expires_after}",
                "-t",
                f"{git.project_name()}:{tag}",
            ]
        )
        assert tag != "dirty", "attempting to push dirty image"
        utils.run_command(
            [
                "podman",
                "push",
                f"{git.project_name()}:{tag}",
                f"quay.io/{QUAY_ORG}/{git.project_name()}:{tag}",
            ]
        )
    return tags
