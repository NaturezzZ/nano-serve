"""Command line entrypoint for nano-serve."""

from __future__ import annotations

import argparse
import json

from nano_serve import __version__
from nano_serve.engine.config import EngineConfig


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nano-serve",
        description="Learning-oriented LLM serving engine.",
    )
    parser.add_argument("--version", action="version", version=f"nano-serve {__version__}")

    subcommands = parser.add_subparsers(dest="command")

    show_config = subcommands.add_parser(
        "show-config",
        help="Print the default engine config as JSON.",
    )
    show_config.set_defaults(func=_show_config)

    subcommands.add_parser("bench", help="Benchmark commands are not implemented yet.")
    subcommands.add_parser("serve", help="Server mode is not implemented yet.")

    return parser


def _show_config(_: argparse.Namespace) -> int:
    print(json.dumps(EngineConfig().to_dict(), indent=2, sort_keys=True))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 0
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())

