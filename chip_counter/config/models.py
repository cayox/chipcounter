# ruff: noqa: D101
from pydantic import BaseModel


class GeneralConfig(BaseModel):
    log_directory: str


class CountingConfig(BaseModel):
    start_count_blue: int
    start_count_red: int


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
