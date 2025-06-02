# config/__init__.py

import os
from dotenv import load_dotenv
from .config_logger import config_logger

"""
Default and basic configurations
"""

# path dirs, order by root
ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DIR_CONFIG: str = rf"{ROOT}/config"
PATH_DIR_LOGS: str = rf"{ROOT}/logs"
PATH_DIR_SCREENSHOTS: str = rf"{ROOT}/screenshots"
PATH_DIR_UTILS: str = rf"{ROOT}/utils"

# path files, order by root
PATH_FILE_LOGS: str = rf"{PATH_DIR_LOGS}/log.log"

# load dotenv
env = load_dotenv()

# pre-loead on import
__all__ = [
    "ROOT",
    "PATH_DIR_CONFIG",
    "PATH_DIR_LOGS",
    "PATH_DIR_SCREENSHOTS",
    "PATH_DIR_UTILS",
    "PATH_FILE_LOGS",
    "env",
    "config_logger",
]
