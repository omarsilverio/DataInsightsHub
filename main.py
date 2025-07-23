import logging
import traceback
import sys
import os
from PyQt5.QtWidgets import QApplication
from src.views.Layout import Layout
from src.utils.Cache import eliminar_cache
from src import config

def main():
    try:
        eliminar_cache()
        app = QApplication(sys.argv)
        with open(os.path.join(config.CSS_PATH, 'style.qss'), 'r', encoding='utf-8') as f:
            app.setStyleSheet(f.read())

        layout = Layout()
        layout.show()

        sys.exit(app.exec_())
    except Exception as e:
        logging.error(f"Error durante el procesamiento: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Error durante el procesamiento: {e}")
        logging.error(traceback.format_exc())
        sys.exit(1)
