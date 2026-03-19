"""CLI argument parser for weatherly."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class Config:
    """Configuration parsed from CLI arguments."""

    city: str
    units: str = "metric"
    days: int = 1


def parse_args() -> Config:
    """Parse command-line arguments and return a Config."""
    parser = argparse.ArgumentParser(
        prog="weatherly",
        description="Fetch weather forecasts from the command line.",
    )
    parser.add_argument("city", help="City name to get weather for")
    parser.add_argument(
        "--units",
        choices=["metric", "imperial"],
        default="metric",
        help="Temperature units (default: metric)",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=1,
        help="Number of forecast days (default: 1)",
    )

    args = parser.parse_args()
    return Config(city=args.city, units=args.units, days=args.days)
