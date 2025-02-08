# SPDX-License-Identifier: ISC
# SPDX-FileCopyrightText: 2025 kurth4cker <kurth4cker@gmail.com>

import argparse
import subprocess

__version__ = "0.1.0"

url = "https://peps.python.org/pep-{:04d}/"
browser = "xdg-open"


def main():
    parser = argparse.ArgumentParser(description="Open peps in browser")
    parser.add_argument(
        "peps",
        help="PEP numbers for opening in browser",
        type=int,
        default=[0],
        nargs=argparse.ZERO_OR_MORE,
    )
    args = parser.parse_args()

    for pep in args.peps:
        subprocess.run((browser, url.format(pep)))


if __name__ == "__main__":
    main()
