import os
import configparser

def get_project_root():
    # El raíz del proyecto sería una carpeta arriba de 'src'
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Leer el archivo config.conf que está en la misma carpeta (src/)
conf_path = os.path.join(os.path.dirname(__file__), 'config.conf')

if not os.path.exists(conf_path):
    raise FileNotFoundError(f"No se encontró config.conf en: {conf_path}")

config = configparser.ConfigParser()
config.read(conf_path)

# Validar que existan las secciones esperadas
if 'Paths' not in config:
    raise KeyError("Falta la sección [Paths] en config.conf")

if 'General' not in config:
    raise KeyError("Falta la sección [General] en config.conf")

# Obtener rutas
raw_root = config['Paths'].get('root_dir', 'PROJECT_ROOT')
ROOT_DIR = get_project_root() if raw_root == 'PROJECT_ROOT' else os.path.abspath(raw_root)

CSS_PATH = os.path.join(ROOT_DIR, config['Paths']['css_dir'])

# Otros valores
APP_TITLE = config['General'].get('app_title', 'Mi Aplicación')
