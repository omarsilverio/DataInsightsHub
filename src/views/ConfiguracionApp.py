import sys
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel

class ConfiguracionApp(QWidget):

    def __init__(self):
        super().__init__()
        contenido_layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: #ecf0f1;")
        contenido_layout.addWidget(QLabel("Configuracion"))