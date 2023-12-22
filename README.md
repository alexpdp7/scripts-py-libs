`scripts-py-libs` is an experiment in building a build tool with PEP-723 for bootstrapping.

You create a `scripts.py` file in the root of the project like:

```
#!/usr/bin/env -S pipx run
# /// pyproject
# run.requirements = ["scripts-py-libs"]
# ///
import spl.python
from spl import __main__
```

This script is executable, and uses pipx as a shebang to work as an executable.
When running `scripts.py`, pipx downloads this library transparently.

Then, you register that you want Python support, by importing `spl.python`.
Finally, you invoke the main entry point of the library.

`spl.python` defines `format` and `validate` subcommands that run Black and Flake8, respectively.

With PEP-723, you can define your own modules like `spl.python`, with your own commands, that you can add as dependencies.
This provides a simple mechanism to reuse code between builds cleanly.

# Caveats

## Issues with PEP-723 in pipx

Due to <https://github.com/pypa/pipx/discussions/1162>, this doesn't work in its intended form yet:

```
$ ./scripts.py format
All done! ✨ 🍰 ✨
4 files left unchanged.
```

For now, you have to:

```
$ poetry run python scripts.py format
All done! ✨ 🍰 ✨
4 files left unchanged.
```

## This is not on pypi

So the requirement dependency in the example above will not work.
I assume you could add a dependency through git.

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
