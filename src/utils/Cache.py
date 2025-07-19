import os
from src import config
import shutil

def eliminar_cache():
    for root, dirs, files in os.walk(config.ROOT_DIR):
        for d in dirs:
            if d == '__pycache__':
                cache_path = os.path.join(root, d)
                print(f"Eliminando: {cache_path}")
                shutil.rmtree(cache_path)