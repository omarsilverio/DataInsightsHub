from PyQt5.QtWidgets import  QToolBar, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from src import config
import os

class MenuBar(QToolBar):

    def __init__(self):
        super().__init__("barra de herramientas")
        self.setMovable(False)
        self._path_icons = os.path.join(config.IMG_PATH, 'icons')
        self._crearBarra()
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    
    def _crearBarra(self):
        # Crear acciones para la barra de herramientas
        accion_nueva = QAction(QIcon(os.path.join(self._path_icons,'nuevo.svg'))," Nuevo", self)
        accion_nueva.setStatusTip("Crear un nuevo archivo")
        accion_nueva.triggered.connect(self._nueva_accion)

        accion_abrir = QAction(QIcon(os.path.join(self._path_icons,'open.svg'))," Abrir", self)
        accion_abrir.setStatusTip("Abrir un archivo existente")
        accion_abrir.triggered.connect(self._abrir_accion)

        # Agregar acciones a la barra de herramientas
        self.addAction(accion_nueva)
        self.addAction( accion_abrir)

    def _nueva_accion(self):
        print("Acción 'Nuevo' seleccionada")

    def _abrir_accion(self):
        print("Acción 'Abrir' seleccionada")

