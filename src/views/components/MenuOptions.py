import os
from src import config
from PyQt5.QtWidgets import QVBoxLayout, QPushButton,QWidget,QSizePolicy
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

class MenuOptions(QWidget):
    # Declaramos una señal personalizada
    boton_presionado = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._path_icons = os.path.join(config.IMG_PATH, 'icons')
        self.setFixedWidth(200)
        self.sidebar_layout = QVBoxLayout(self)

        self.opciones = [
            ("  Inicio", "house.svg", "btn_inicio"),
            ("  Dashboard", "chart-pie.svg", "btn_dashboard"),
            ("  Datos", "table.svg", "btn_datos"),
            ("  Configuración","gear.svg", "btn_config"),
        ]
        
        for label, icon_name, attr_name in self.opciones:
            btn = self._crearButton(label, icon_name,attr_name)
            setattr(self, attr_name, btn)  # Guarda el botón como atributo: self.btn_inicio, etc.
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.sidebar_layout.addWidget(btn)

        self.sidebar_layout.addStretch()

    def _crearButton(self,label: str, name_icon: str,name_button: str) -> QPushButton:
        btn_aux =  QPushButton(label)
        btn_aux.setIcon(QIcon(os.path.join(self._path_icons, name_icon)))
        btn_aux.setObjectName("BotonMenuOption")
        btn_aux.clicked.connect(lambda _, n=name_button: self.boton_presionado.emit(n))

        return btn_aux

    def resaltar_boton(self, nombre_boton):
        for _, _, attr_name in self.opciones:
            btn = getattr(self, attr_name)
            estilo = "background-color: #0078D7; color: white;" if attr_name == nombre_boton else ""
            btn.setStyleSheet(estilo)


       

