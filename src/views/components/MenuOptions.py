from PyQt5.QtWidgets import QAction, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QWidget,QSizePolicy
import os
from src import config
from PyQt5.QtGui import QIcon

class MenuOptions(QWidget):
    def __init__(self):
        super().__init__()
        self._path_icons = os.path.join(config.IMG_PATH, 'icons')
        #self.main_layout = QHBoxLayout(self)

         # ===== Barra lateral personalizada =====
        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(200)
        self.sidebar_layout = QVBoxLayout(self.sidebar)

         # Estilo simple
        self.sidebar.setStyleSheet("background-color: #2c3e50; color: white;")
        
        # Botones de la barra lateral
        btn_inicio = QPushButton("  Inicio")
        btn_inicio.setIcon(QIcon(os.path.join(self._path_icons, 'house.svg')))
        btn_dashboard = QPushButton("  Dashboard")
        btn_dashboard.setIcon(QIcon(os.path.join(self._path_icons, 'chart-pie.svg')))
        btn_datos = QPushButton("  Datos")
        btn_datos.setIcon(QIcon(os.path.join(self._path_icons, 'table.svg')))
        btn_config = QPushButton("  Configuración")
        btn_config.setIcon(QIcon(os.path.join(self._path_icons, 'gear.svg')))


        for btn in [btn_inicio, btn_dashboard,btn_datos, btn_config]:
            btn.setStyleSheet("""
                QPushButton {
                    padding: 10px;
                    text-align: left;
                    background-color: #34495e;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #3d566e;
                }
            """)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.sidebar_layout.addWidget(btn)

        self.sidebar_layout.addStretch()

         # ===== Área de contenido principal =====
        contenido = QWidget()
        contenido_layout = QVBoxLayout(contenido)
        contenido.setStyleSheet("background-color: #ecf0f1;")
        contenido_layout.addWidget(QLabel("Contenido principal"))

        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(contenido)

