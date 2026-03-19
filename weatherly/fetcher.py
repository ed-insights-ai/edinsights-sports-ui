from dataclasses import dataclass

import requests


@dataclass
class Config:
    api_key: str
    base_url: str = "https://api.openweathermap.org/data/2.5"
    units: str = "metric"
    city: str = "London"


def fetch_weather(config: Config) -> dict:
    """Fetch current weather data for the configured city."""
    params = {
        "q": config.city,
        "appid": config.api_key,
        "units": config.units,
    }
    response = requests.get(f"{config.base_url}/weather", params=params)
    response.raise_for_status()
    return response.json()
