from argparse import ArgumentParser
from imktk.dataarray_methods import anomalies
from imktk import main as version

DATAARRAY_METHODS = [
    anomalies,
]

cli = ArgumentParser(prog="imktk", description="CLI tool for the IMK-toolkit")
subparsers = cli.add_subparsers(dest="subcommand")

for module in DATAARRAY_METHODS:
    name = module.__name__.rsplit(".", 1)[1]
    subcommand = subparsers.add_parser(name, description=module.main.__doc__)
    for arg in module._arguments():
        subcommand.add_argument(*arg[0], **arg[1])
    subcommand.set_defaults(func=module._cli)

sc = subparsers.add_parser("version", description="Print version of tool")
sc.set_defaults(func=version)


def main():
    args = cli.parse_args()
    if args.subcommand is None:
        cli.print_help()
    else:
        args.func(args)
