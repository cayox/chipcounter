#!/bin/bash
set -x #echo on

rsync -rav -e ssh . admin@192.168.86.28:/home/admin/dev/chip_counter/ --include="*.py" --include='*.ttf' --include='*.svg' --include='*.png' --include='*.toml' --include='*.qss' --include='*.sh' --exclude='__pycache__/*' --exclude='.git/*' --exclude='.idea/*' --exclude='.ruff_cache/*' --exclude='*.s*'