# Clase padre para los layouts principales
import os
from src import config
from .MetaWidget import MetaWidget
from abc import abstractmethod
from PyQt5.QtWidgets import QWidget, QApplication


class Layout(QWidget, metaclass=MetaWidget):
    def __init__(self, titulo="Mi Aplicación", tamanio_ventana=None):
        super().__init__()        
        self.titulo = titulo
        self._iniciarConfiguracion(tamanio_ventana)

    def _iniciarConfiguracion(self,tamanio_ventana):
        self._setTamanioVentana(tamanio_ventana)
        self.setWindowTitle(self.titulo)
        self.resize(*self.tamanio_ventana)
    
    def _setTamanioVentana(self,tamanio_ventana):
        if tamanio_ventana is None:
            size = QApplication.instance().primaryScreen().size()
            self.tamanio_ventana = (size.width(), size.height())
        else:
            self.tamanio_ventana = tamanio_ventana

    @abstractmethod
    def iniciar(self):
        pass