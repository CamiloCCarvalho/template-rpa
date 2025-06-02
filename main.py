from rpa_suite import rpa
from rpa_suite.utils import system
import config

def main(config=config) -> None:
    
    try:

        # your code here
        rpa.log.log_start_run_debug(f'Start bot')
        rpa.log.log_info(f'Tasks screenshot in execution')
        rpa.file.screen_shot()
        rpa.log.log_debug(f'Bot finished')
        # finish your code here

    except Exception as e:
        rpa.log.log_error(f'Erro durante a função: {main.__name__}! Error: {str(e)}.')

if __name__ == '__main__':

    with system.KeepSessionActive(): # keep session active
        main()
