from abc import ABCMeta
from PyQt5.QtWidgets import QWidget

class MetaWidget(ABCMeta, type(QWidget)):
    pass