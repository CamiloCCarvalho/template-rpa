# ./utils/del_cache.py

import os
import shutil
from rpa_suite import rpa
from config.config_logger import config_logger

def delete_pycache(directory: str = '.') -> None:
    
    """
    Function Responsible to delete all pycache on project
    """
    
    try:
        # Percorrer a árvore de diretórios
        for root, dirs, files in os.walk(directory):

            # Se '__pycache__' estiver na lista de diretórios
            if '__pycache__' in dirs:
                
                # Construir o caminho completo para o diretório '__pycache__'
                pycache_dir = os.path.join(root, '__pycache__')
                
                # Remover o diretório '__pycache__' e todo o seu conteúdo
                shutil.rmtree(pycache_dir)

    except Exception as e:
        rpa.log.log_error(f'Erro durante a função: {delete_pycache.__name__}! Error: {str(e)}')
