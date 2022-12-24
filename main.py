from __future__ import annotations

import asyncio
import json
import logging
from dataclasses import dataclass
from datetime import datetime
from typing import List
from api import GoveeClient
from colors import *

MONITOR_LIGHT = '61:40:D2:39:32:37:2D:73'
client = GoveeClient()
logging.basicConfig(level=logging.INFO)


async def colors():
    client = GoveeClient()
    await client.turn_on(MONITOR_LIGHT)
    await client.set_brightness(MONITOR_LIGHT, 100)
    await client.set_color_by_rgb(MONITOR_LIGHT, GREEN)

    await asyncio.sleep(5)
    await client.set_color_by_rgb(MONITOR_LIGHT, RED)
    await client.set_color_by_rgb(MONITOR_LIGHT, GREEN)
    await client.set_color_by_rgb(MONITOR_LIGHT, BLUE)
    await client.set_color_by_rgb(MONITOR_LIGHT, PURPLE)
    await client.turn_off(MONITOR_LIGHT)


@dataclass
class ColorConfig:
    """

        color: Color to set the light to
        duration: How long to keep the light on for in milliseconds
        time_start: When to start the light
        time_end: When to turn off the light
        brightness: Brightness of the light

    """
    color: Color
    duration: int | float
    time_start: datetime
    time_end: datetime
    brightness: int = 100

    def to_json(self):
        return {
            "color": self.color,
            "duration": self.duration,
            "time_start": self.time_start,
            "time_end": self.time_end,
            "brightness": self.brightness

        }

    @classmethod
    def load(cls, data: dict) -> ColorConfig:
        cls.color = data["color"]
        cls.duration = data["duration"]
        cls.time_start = data["time_start"]
        cls.time_end = data["time_end"]
        cls.brightness = data["brightness"]
        return cls


class LightConfig:
    def __init__(self, configs: List[ColorConfig] | ColorConfig):
        self.configs = configs

    def to_json(self):
        return {
            "configs": [config.to_json() for config in self.configs]
        }

    def save(self, name: str):
        with open(f'./configs/{name}.json', "w+") as f:
            json.dump(self.to_json(), indent=4, fp=f)

    def load(self, name: str):
        with open(f'./configs/{name}.json', "r") as f:
            data = json.load(f)
            self.configs = [ColorConfig.load(config) for config in data["configs"]]


# scheduler.scheduled_job('interval', hour=1)
async def morning_routine():
    await client.turn_on(MONITOR_LIGHT)
    await client.set_brightness(MONITOR_LIGHT, 100)
    await client.set_color_by_rgb(MONITOR_LIGHT, GREEN)
    await asyncio.sleep(5)
    await client.turn_off(MONITOR_LIGHT)


async def main():
    await colors()


if __name__ == "__main__":
    asyncio.run(main())
