from rpa_suite.log.functions_logger_uru import *
from rpa_suite import suite as rpa
from config.config_logger import config_logger

def main(config_logger=config_logger) -> None:
    
    try:
        
        # your code here
        log_start_run_debug(f'Start bot')
        log_info(f'Tasks screenshot in execution')
        rpa.screen_shot()
        log_debug(f'Bot finished')
        ...
        
    except Exception as e:
        log_error(f'Erro durante a função: {main.__name__}! Error: {str(e)}')

if __name__ == '__main__':
    main()