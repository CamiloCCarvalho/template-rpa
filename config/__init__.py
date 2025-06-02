# config/__init__.py

import os
import dotenv
from .config_logger import config_logger

# pylint: disable=pointless-string-statement
""" 
Default and basic configurations
"""
# pylint: disable=pointless-string-statement

# path dirs, order by root
ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DIR_CONFIG: str = rf"{ROOT}/config"
PATH_DIR_LOGS: str = rf"{ROOT}/logs"
PATH_DIR_MODULES: str = rf"{ROOT}/modules"
PATH_DIR_SCREENSHOTS: str = rf"{ROOT}/screenshots"
PATH_DIR_UTILS: str = rf"{ROOT}/utils"

# path files, order by root
PATH_FILE_LOGS: str = rf"{PATH_DIR_LOGS}/log.log"

# load dotenv
_env = dotenv.load_dotenv()

# pre-loead on import
__all__ = [
    "ROOT",
    "PATH_DIR_CONFIG",
    "PATH_DIR_LOGS",
    "PATH_DIR_SCREENSHOTS",
    "PATH_DIR_UTILS",
    "PATH_FILE_LOGS",
    "_env",
    "config_logger",
]
