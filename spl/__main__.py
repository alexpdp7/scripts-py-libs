import argparse

import spl


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)

for command in spl.commands:
    subparser = subparsers.add_parser(command.__name__)
    subparser.set_defaults(func=command)


args = parser.parse_args()
args.func(args)
