import sys
from .Layout import Layout
from PyQt5.QtWidgets import QPushButton, QMessageBox

class DashboardApp(Layout):

    def __init__(self):
        super().__init__(titulo="Dashboard")
        self.iniciar()

    def iniciar(self):
        self.construirDashboard()

    def onClick(self):
        QMessageBox.information(self, "Mensaje", "¡Hola! Has hecho clic en el botón.")

    def crearBoton(self):
        boton = QPushButton("Haz clic aquí", self)
        boton.clicked.connect(self.onClick)
        boton.resize(150, 40)
        boton.move(75, 80)

    def construirDashboard(self):
        self.crearBoton()