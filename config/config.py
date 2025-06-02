# ./config/config.py
import os

"""
Default and basic configurations
"""

# path dirs, order by root
ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DIR_CONFIG: str = fr'{ROOT}/config'
PATH_DIR_LOGS: str = fr'{ROOT}/logs'
PATH_DIR_SCREENSHOTS: str = fr'{ROOT}/screenshots'
PATH_DIR_UTILS: str = fr'{ROOT}/utils'

# path files, order by root
PATH_FILE_LOGS: str = fr'{PATH_DIR_LOGS}/log.log'

