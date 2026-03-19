from dataclasses import dataclass


@dataclass
class WeatherData:
    """Weather observation data for a specific location."""

    location: str
    temperature_c: float
    temperature_f: float
    feels_like_c: float
    humidity: int
    description: str
    wind_speed_kph: float
    wind_direction: str
    is_day: bool

    def __str__(self) -> str:
        period = "Day" if self.is_day else "Night"
        return (
            f"{self.location}: {self.description}, "
            f"{self.temperature_c}°C ({self.temperature_f}°F), "
            f"feels like {self.feels_like_c}°C, "
            f"humidity {self.humidity}%, "
            f"wind {self.wind_speed_kph} kph {self.wind_direction}, "
            f"{period}"
        )
