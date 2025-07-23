# Clase padre para los layouts principales
import os
from src import config
from .components.MenuBar import MenuBar
from .components.MenuOptions import MenuOptions
from .DashboardApp import DashboardApp
from .ConfiguracionApp import ConfiguracionApp
from .DatosApp import DatosApp
from .InicioApp import InicioApp
from abc import abstractmethod
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QLabel,QWidget


class Layout(QMainWindow):
    def __init__(self, titulo="Mi Aplicación", tamanio_ventana=None):
        super().__init__()
        #por default
        self._contenido_seleccionado = 'btn_dashboard';
        self.titulo = titulo
        self._iniciarConfiguracion(tamanio_ventana)

        self.central_widget = QWidget()
        self.menu_options = MenuOptions()
        self._main_layout = QHBoxLayout()

         # Diccionario de botones a clases de contenido
        self._contenidos = {
            'btn_dashboard': DashboardApp,
            'btn_inicio': InicioApp,
            'btn_config': ConfiguracionApp,
            'btn_datos': DatosApp,
        }
        
        self._contenido = self._contenidos[self._contenido_seleccionado]()
        self.menu_options.resaltar_boton(self._contenido_seleccionado)

        self._main_layout.addWidget(self.menu_options)
        self._main_layout.addWidget(self._contenido)

        self.central_widget.setLayout(self._main_layout)
        self.setCentralWidget(self.central_widget)

        self.menu_options.boton_presionado.connect(self.menu_click)

    def menu_click(self, nombre_boton):
        if self._contenido_seleccionado == nombre_boton:
            return

        self._limpiarContenido()
        self._contenido_seleccionado = nombre_boton
         # Notificar a MenuOptions para resaltar
        self.menu_options.resaltar_boton(nombre_boton)

        if nombre_boton in self._contenidos:
            self._contenido = self._contenidos[nombre_boton]()
            self._main_layout.addWidget(self._contenido)

    def _iniciarConfiguracion(self,tamanio_ventana):
        self._setTamanioVentana(tamanio_ventana)
        self.setWindowTitle(self.titulo)
        self.resize(*self.tamanio_ventana)
        self._crearBarraHerramientas()
    
    def _setTamanioVentana(self,tamanio_ventana):
        if tamanio_ventana is None:
            size = QApplication.instance().primaryScreen().size()
            self.tamanio_ventana = (size.width(), size.height())
        else:
            self.tamanio_ventana = tamanio_ventana
    
    def _crearBarraHerramientas(self):
        barra_herramientas = MenuBar();
        self.addToolBar(barra_herramientas)
    
    def _limpiarContenido(self):
        self._main_layout.removeWidget(self._contenido)
        self._contenido.setParent(None)
        self._contenido.deleteLater()
        self._contenido = None  
       