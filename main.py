import logging
import traceback
import sys
from PyQt5.QtWidgets import QApplication
from src.views.DashboardApp import DashboardApp

def main():
    try:
        app = QApplication(sys.argv)
        dashboard = DashboardApp()
        dashboard.show()
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
