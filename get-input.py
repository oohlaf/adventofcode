#!/usr/bin/env python3

import argparse
import logging
import os
import sys

from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen


log = logging.getLogger()
logging_configured = False
log_levels = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}


def configure_logging(args):
    global logging_configured
    if not logging_configured:
        log.setLevel(log_levels[args.log_level])
        console_log = logging.StreamHandler(stream=sys.stderr)
        log.addHandler(console_log)
        logging_configured = True


def main():
    SESSION = os.environ.get("SESSION", None)
    if not SESSION:
        # You can find SESSION by using Chrome tools:
        # 1) Go to https://adventofcode.com/2022/day/1/input
        # 2) right-click -> inspect -> click "Network".
        # 3) Refresh
        # 4) Click click
        # 5) Click cookies
        # 6) Grab the value for session. Fill it in.
        log.fatal("No SESSION environment variable defined!")
        return 1
    else:
        log.debug("SESSION defined")

    today = datetime.today()
    parser = argparse.ArgumentParser(description="Read input")
    parser.add_argument("--log-level", metavar="LEVEL", choices=log_levels.keys(), default="info")
    parser.add_argument("--year", type=int, default=today.year)
    parser.add_argument("--day", type=int, default=today.day)
    args = parser.parse_args()
    configure_logging(args)

    log.info("Downloading Advent of Code input for Year %s Day %s", args.year, args.day)

    req = Request(f"https://adventofcode.com/{args.year}/day/{args.day}/input")
    req.add_header("Cookie", f"session={SESSION}")
    req.add_header("User-Agent", "AoC get input script")

    with urlopen(req) as res:
        data = res.read()

    charset = res.headers.get_content_charset()
    if not charset:
        charset = "utf-8"
    decoded_body = data.decode(charset)
    lines = decoded_body.count("\n")
    log.debug("input data\n%s", decoded_body)

    aoc_path = Path(f"{args.year}/day{args.day:02d}")
    aoc_input = aoc_path / "input.txt"

    aoc_path.mkdir(parents=True, exist_ok=True)
    with open(aoc_input, mode="wb") as input_file:
        input_file.write(data)

    log.info("File: %s", aoc_input)
    log.info("Lines: %s", lines)


if __name__ == "__main__":
    exit(main())
