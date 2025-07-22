# Clase padre para los layouts principales
import os
from src import config
from .MetaMainWindow import MetaMainWindow
from .components.MenuBar import MenuBar
from .components.MenuOptions import MenuOptions
from abc import abstractmethod
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QWidget,QSizePolicy


class Layout(QMainWindow, metaclass=MetaMainWindow):
    def __init__(self, titulo="Mi Aplicación", tamanio_ventana=None):
        super().__init__()        
        self.titulo = titulo
        self._iniciarConfiguracion(tamanio_ventana)

        # Crear widget central y layout principal
        self.central_widget = MenuOptions()
        self.main_layout = QHBoxLayout()
        
        self.setCentralWidget(self.central_widget)


    def _iniciarConfiguracion(self,tamanio_ventana):
        self._setTamanioVentana(tamanio_ventana)
        self.setWindowTitle(self.titulo)
        self.resize(*self.tamanio_ventana)
        self.crearBarraHerramientas()
    
    def _setTamanioVentana(self,tamanio_ventana):
        if tamanio_ventana is None:
            size = QApplication.instance().primaryScreen().size()
            self.tamanio_ventana = (size.width(), size.height())
        else:
            self.tamanio_ventana = tamanio_ventana
    
    def crearBarraHerramientas(self):
        barra_herramientas = MenuBar();
        self.addToolBar(barra_herramientas)
       

    @abstractmethod
    def iniciar(self):
        pass