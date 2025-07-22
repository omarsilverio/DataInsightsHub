from abc import ABCMeta
from PyQt5.QtWidgets import QMainWindow

class MetaMainWindow(ABCMeta, type(QMainWindow)):
    pass