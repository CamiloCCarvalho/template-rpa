
from rpa_suite import rpa
from config.config_logger import config_logger

def main(config_logger=config_logger) -> None:
    
    try:
        
        # your code here
        rpa.log.log_start_run_debug(f'Start bot')
        rpa.log.log_info(f'Tasks screenshot in execution')
        rpa.file.screen_shot()
        rpa.log.log_debug(f'Bot finished')
        ...
        
    except Exception as e:
        rpa.log.log_error(f'Erro durante a função: {main.__name__}! Error: {str(e)}')

if __name__ == '__main__':
    main()
