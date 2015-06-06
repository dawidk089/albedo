__author__ = 'mcmushroom'

import sys
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtGui import *

class Map(QtGui.QWidget):

    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.map = QImage(x, y, QImage.Format_RGB32)
        self.pixel = []

        self.init_pixels(0, 0, 0)
        self.set_pixels()

    def init_pixels(self, r, g, b):
        for i in range(0, self.y):
            temp_tab = []
            for j in range(0, self.y):
                temp_tab.append(qRgb(r, g, b))
            self.pixel.append(temp_tab)

    def set_pixels(self):
        for i in range(0, self.y):
            for j in range(0, self.y):
                self.map.setPixel(i, j, self.pixel[i][j])

    def get(self):
        return self.map