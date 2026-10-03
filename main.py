"""Eset Desktop — Keep Eset data folders on disk: dated copies of config and export files before a patch."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='eset_desktop',
        description='Keep Eset data folders on disk: dated copies of config and export files before a patch.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Eset Desktop')
    print('Archive Eset files on this machine before you change the install.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
