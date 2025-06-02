# ./config/config_logger.py

try:
    """
    Module responsible for instance logger, create dir, create file, and configurate stream_handler and file_handler
    """

    from rpa_suite import rpa

    config_logger = rpa.log.config_logger()

except Exception as e:
    rpa.error_print(f'Erro durante processmaento do arquivo em: "config/config_looger.py"! Error: {str(e)}')
