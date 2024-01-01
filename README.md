`scripts-py-libs` is a build tool experiment, designed with PEP-723 in mind.

# Usage

I have not been able to use PEP-723 yet.
I think `pipx` support is close, but not ready yet for this use case.
In the meantime, you can use this project with some hacks.

Add this repo as a submodule:

```
$ git submodule add https://github.com/alexpdp7/scripts-py-libs.git .scripts-py-libs
```

Create a `scripts.py` file in the root of the project like:

```
#!/usr/bin/env python3
import os, subprocess, sys

if not os.environ.get("SCRIPTS_PY_LIBS_BOOTSTRAPPED"):
    sys.exit(subprocess.run([".scripts-py-libs/bootstrap"] + sys.argv).returncode)

import spl.python
from spl import __main__
```

This script is executable, and uses a bootstrap script to simulate PEP-723.

Then, you register that you want Python support, by importing `spl.python`.
Finally, you invoke the main entry point of the library.

`spl.python` defines `format` and `validate` subcommands that run Black and Flake8, respectively.

With PEP-723, instead of using the bootstrap script, you will be able to depend on this module directly.
You will also be able to depend on other modules which add more reusable commands.

# Future ideas

## Dependencies

Subcommands could depend on each other for chaining of jobs.
For example, run tests after linting successfully.

Also commands could define which files they use as inputs and outputs, and only run if inputs change.

## Standard interfaces

`spl.python` and `spl.rust` can both define a `format` tasks.
This makes working across projects easier.

`spl.python` could detect multiple linters, or different ways to set up projects (either automatically or through configuration).

## Recursive scripts

Top-level `scripts.py` scripts can locate other `scripts.py` on subdirectories and propagate tasks.

## Drivers

Commands might define different implementations.
For example, a command that runs some task could have a Docker implementation and a Kubernetes implementation.

Depending on your environment, you might configure the use of different implementations.
So in a local offline environment, you might run the task using Docker.
But when in an online environment with a large Kubernetes cluster available, you might choose to use the Kubernetes implementation.

## Parallelization

...

## Alternative frontends

With parallel builds, instead of sending everything to the console, you could spin up a small web server.
This web server could let you see the output of different commands which were executed in parallel, separately.

## Automation tool

An automation tool which was aware of this library could run scripts intelligently, allowing you to view the outputs of different build steps separately, etc.
