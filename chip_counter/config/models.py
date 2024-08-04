# ruff: noqa: D101
import os.path
import tomllib

import toml
from pydantic import BaseModel


class GeneralConfig(BaseModel):
    log_directory: str


class CountingConfig(BaseModel):
    chip_factor: float
    motor_duration: int
    seperate_motors: bool


class RaspberryPiConfig(BaseModel):
    sensor_bounce_time: int

    count_sensor1_pin: int
    count_sensor2_pin: int
    motor1_trigger_sensor: int
    motor1_pin: int
    motor2_trigger_sensor: int
    motor2_pin: int

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
    admin_password: str

    save_interval: int  # in minutes


class Config(BaseModel):
    general: GeneralConfig
    colors: ColorsConfig
    ui: UiConfig
    counting: CountingConfig
    raspberry_pi: RaspberryPiConfig

    @classmethod
    def load_toml(cls: "Config", toml_path: str) -> "Config":
        """Class method to load the config from a toml file."""
        with open(toml_path, "rb") as f:
            toml = tomllib.load(f)

            return cls(**toml)

    def save(self, filepath: str) -> None:
        """Save config to `filepath` (as toml)."""
        if os.path.isfile(filepath):
            os.remove(filepath)

        with open(filepath, "w+") as f:
            toml.dump(self.dict(), f)
