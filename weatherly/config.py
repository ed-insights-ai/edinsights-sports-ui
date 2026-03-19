"""Weatherly configuration module.

Defines API configuration constants and a Config dataclass for
managing weather service settings.
"""

from dataclasses import dataclass, field

API_BASE_URL: str = 'https://wttr.in'
DEFAULT_FORMAT: str = 'j1'
DEFAULT_UNITS: str = 'metric'
REQUEST_TIMEOUT: int = 10


@dataclass
class Config:
    """Configuration for weatherly requests."""

    location: str = ''
    units: str = DEFAULT_UNITS
    format: str = DEFAULT_FORMAT
