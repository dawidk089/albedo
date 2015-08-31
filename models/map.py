__author__ = 'mcmushroom'

import sys
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtGui import *

class Map(QtGui.QWidget):

    def __init__(self, x, y):
        super().__init__()

        self.pixel = []
        self.x = x
        self.y = y
        self.map = QImage(self.y, self.x, QImage.Format_RGB32)

    def init_pixels(self, table, t_min, t_range):
        self.pixel = []
        for row in table:
            temp_tab = []
            for item_pix in row:
                """
                temp_tab.append(qRgb(
                    int((item_pix['r']-t_min)/t_range*255),
                    int((item_pix['g']-t_min)/t_range*255),
                    int((item_pix['b']-t_min)/t_range*255),
                ))
                """
                temp_tab.append(qRgb(
                    int((item_pix['r']-t_min)/t_range*255),
                    0,
                    255-int((item_pix['g']-t_min)/t_range*255),
                ))
            self.pixel.append(temp_tab)

    def set_pixels(self):
        print('x pixel:', len(self.pixel))
        print('y pixel:', len(self.pixel[0]))
        print('x iter:', self.x)
        print('y iter:', self.y)
        for i in range(0, self.x):
            for j in range(0, self.y):
                self.map.setPixel(j, i, self.pixel[i][j])

    def init_pixels0(self):
        self.pixel = []
        for i in range(self.x):
            temp_tab = []
            for j in range(self.y):
                temp_tab.append(qRgb(255, 255, 255))
            self.pixel.append(temp_tab)