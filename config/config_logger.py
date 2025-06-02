# ./config/config_logger.py

try:
    # pylint: disable=pointless-string-statement
    """
    Module responsible for instance logger, create dir, create file, and configurate stream_handler and file_handler
    """
    # pylint: disable=pointless-string-statement

    from rpa_suite import rpa

    config_logger = rpa.log.config_logger()

except Exception as e:
    rpa.error_print(f'Erro durante processmaento do arquivo em: "config/config_looger.py"! Error: {str(e)}')
