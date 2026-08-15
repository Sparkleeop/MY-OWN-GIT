import argparse, sys
from pathlib import Path

from commands.init import init

class Repository:
    def __init__(self, path="."):
        self.path = Path(path).resolve() # git init

def main():
    parser = argparse.ArgumentParser(
        description="GIT - My own GIT client"
    )

    subparsers = parser.add_subparsers(dest="command", help="an available command")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize a new repository")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return
    try:
        if args.command == "init":
            pass
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

main()