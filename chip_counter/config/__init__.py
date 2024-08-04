import csv
import os.path
import shutil
import sys
import tomllib

from .models import Config


def get_application_path() -> str:
    """Return the path of the application."""
    if getattr(sys, "frozen", False):
        return sys._MEIPASS  # noqa: SLF001
    return os.path.abspath(os.path.dirname(sys.modules["__main__"].__file__))


APP_CONFIG_ROOT = os.path.expanduser("~/chip_counter")

ASSETS = os.path.join(get_application_path(), "assets")


def checkout_files() -> None:
    """Check if necessary files are in APP_CONFIG_ROOT and copy them there if not."""
    os.makedirs(APP_CONFIG_ROOT, exist_ok=True)

    dirs_to_checkout = ["img", "icons"]
    for checkout_dir in dirs_to_checkout:
        dst = os.path.join(APP_CONFIG_ROOT, checkout_dir)
        if not os.path.isdir(dst):
            src = os.path.join(ASSETS, checkout_dir)
            shutil.copytree(src, dst)

    config_path = os.path.join(APP_CONFIG_ROOT, "config.toml")
    if not os.path.isfile(config_path):
        src = os.path.join(ASSETS, "config.toml")
        shutil.copy(src, APP_CONFIG_ROOT)


checkout_files()

CONFIG_PATH = os.path.join(APP_CONFIG_ROOT, "config.toml")
CONFIG = Config.load_toml(CONFIG_PATH)
