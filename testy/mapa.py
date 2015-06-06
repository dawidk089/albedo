# -*- coding: utf-8 -*-
__author__ = 'mcmushroom'

import sys
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtGui import *
from view.map import Map


class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.map = Map(100, 100)
        self.map.init_pixels(0, 0, 0)
        self.map.set_pixels()

        self.label = QtGui.QLabel()
        self.label.setPixmap(QPixmap.fromImage(self.map.get()))

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        hbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


    # definicja podpiec
    def slot_conn(self, slots={}):
        for key in slots:
            self.button[key].clicked.connect(slots[key])
            print(">checkpoint: slots plugging for key: ", key, 'in class: ', self.__class__.__name__)


    # pomocnicza metoda do budowania layout'u
    def box(self, el_type, elems):

        if el_type == 'vertical':
            box = QtGui.QVBoxLayout()

        elif el_type == 'horizontal':
            box = QtGui.QHBoxLayout()

        for elem in elems:
            if elem[0] == 'widget':
                box.addWidget(elem[1])
            elif elem[0] == 'layout':
                box.addLayout(elem[1])
            elif elem[0] == 'stretch':
                box.addStretch(1)

        return box

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()