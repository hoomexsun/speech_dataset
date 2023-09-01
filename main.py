import argparse
from config.project import setup_arg_parser
from dataset import DatasetProject
from describe import describe
from gui import gui


def main():
    project = DatasetProject()
    project.run()


# -------------------------------- SCRIPT MODE -------------------------------- #
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Main method")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-g", "--gui", action="store_true", help="Access GUI mode")
    group.add_argument(
        "-d", "--desc", action="store_true", help="Describe dataset info"
    )
    args = parser.parse_args()

    if args.gui:
        gui()
    elif args.desc:
        describe()
    else:
        main()
