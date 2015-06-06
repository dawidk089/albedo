# -*- coding: utf-8 -*-
__author__ = 'mcmushroom'

import sys
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtGui import *
from view.map import Map


class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.header = QLabel('<h1><b>Albedo Ziemi</b></h1>', self)

        self.map = Map(800, 600)
        self.map.init_pixels(0, 0, 0)
        self.map.set_pixels()
        self.map_item = QtGui.QLabel()
        self.map_item.setPixmap(QPixmap.fromImage(self.map.get()))

        self

        self.initUI()

    # inicjalizacja widget'ow i layout'u
    def initUI(self):

        #layout
        header_l = [
            ('stretch',),
            ('widget', self.header),
            ('stretch',),
        ]

        self.header_box = self.box('horizontal', header_l)

        main_l = [
            ('layout', self.header_box),
            ('widget', self.map_item),
        ]

        self.mainbox = self.box('vertical', main_l)

        self.setLayout(self.mainbox)

        self.show()

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
