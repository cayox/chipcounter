# ruff: noqa: D101
import os.path
import json
import toml

from pydantic import BaseModel


class GeneralConfig(BaseModel):
    log_directory: str


class CountingConfig(BaseModel):
    start_count_blue: int
    start_count_red: int
    chip_factor: float
    motor_duration: int


class RaspberryPiConfig(BaseModel):
    sensor_pin1: int
    ctrl_sensor_pin1: int
    sensor_pin2: int
    ctrl_sensor_pin2: int
    motor_pin: int

    button_engine_pin: int
    button_reset_pin: int
    mode_switch_pin1: int
    mode_switch_pin2: int


class ColorsConfig(BaseModel):
    background_color: str
    text_color: str

    accent1_light: str
    accent1: str
    accent1_dark: str

    accent2_light: str
    accent2: str
    accent2_dark: str

    icon_color: str

    white: str
    red: str

    disabled_light: str
    disabled: str
    disabled_dark: str


class UiConfig(BaseModel):
    text_counter1: str
    text_counter2: str
    text_counter_global: str


class Config(BaseModel):
    general: GeneralConfig
    colors: ColorsConfig
    ui: UiConfig
    counting: CountingConfig
    raspberry_pi: RaspberryPiConfig

    def save(self, filepath: str):
        """Save config to `filepath` (as toml)."""
        if os.path.isfile(filepath):
            os.remove(filepath)

        with open(filepath, "w+") as f:
            toml.dump(self.dict(), f)
