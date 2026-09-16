#!/usr/bin/env python3
"""Create a safe starter workspace for a travel-planning project."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a travel project from the bundled template."
    )
    parser.add_argument("output", type=Path, help="New project directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.expanduser().resolve()
    template = Path(__file__).resolve().parent.parent / "assets" / "project-template"

    if not template.is_dir():
        raise SystemExit(f"Template directory is missing: {template}")
    if output.exists():
        raise SystemExit(
            f"Refusing to overwrite existing path: {output}\n"
            "Choose a new project directory."
        )

    shutil.copytree(template, output)
    for relative in ("outputs/guide", "outputs/map", "outputs/pdf"):
        (output / relative).mkdir(parents=True, exist_ok=True)

    print(f"Created travel project: {output}")
    print("Next: complete trip-brief.yaml, research sources, and data/trip-data.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
