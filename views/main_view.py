# -*- coding: utf-8 -*-
__author__ = 'mcmushroom'

import sys
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtGui import *
from models.map import Map
from models.data_storage import DataStorage
from calls.calling import Calling
from paths import project_path as p


class MainWindow(QtGui.QWidget):

    def __init__(self, main):
        super(MainWindow, self).__init__()

        self.main = main

        # init sets
        self.width_editline = 100

        # utworzenie obiektu pod wywolanie symulatora
        self.wywolanie = Calling(p()+'/symulator/wersja6')
        
        # naglowek
        self.header = QLabel('<h1><b>Albedo Ziemi</b></h1>', self)

        # mapa
        """
        # # odczyt pliku
        self.map_data = DataStorage('../../dane/temperatura_0.txt')
        self.x = self.map_data.rows
        self.y = self.map_data.columns

        self.min_temp = float('inf')
        self.max_temp = 0
        """

        # # zadeklarowanie wymiarow mapy
        #self.map = Map(self.x, self.y)
        self.map = Map(600, 800)

        # # definicja tablicy rgb
        self.rgb = []
        self.map.init_pixels0()

        """
        self.temp_to_rgb()

        #zmieniam recznie max, min
        #self.min_temp = 300
        #self.max_temp = 400

        # # definicja obrazu mapy
        self.range_temp = self.max_temp-self.min_temp
        self.map.init_pixels(self.rgb, self.min_temp, self.range_temp)
        """
        # # nalozenie obrazu na mape
        self.map.set_pixels()

        self.map_item = QtGui.QLabel()

        self.width_map = self.screen_size()['w']-self.width_editline
        self.height_map = self.screen_size()['h']*self.width_editline

        self.map_item.setScaledContents(True)
        self.map_item.setPixmap(QPixmap.fromImage(self.map.map))

        # check button
        self.sun = QCheckBox('słońce')
        self.emision = QCheckBox('emisja')
        self.heat = QCheckBox('przewodnictwo')

        # editline
        self.editlines = {
            'calls': QLineEdit(self),
            'albedo_land': QLineEdit(self),
            'albedo_sea': QLineEdit(self),
            'coof_reemision': QLineEdit(self),
            'coof_dyfusion': QLineEdit(self),
            'sun_const': QLineEdit(self),
            'meridian_amount': QLineEdit(self),
            'parallel_amount': QLineEdit(self),
        }

        # labels
        #self.meridian_amount = QLabel('ilość południków: '+str(0), self)
        #self.parallel_amount = QLabel('ilość równoleżników: '+str(0), self)
        self.time = QLabel('czas: '+str(0), self)

        # button
        self.button = {}

        self.button["generate"] = QPushButton('Generuj')
        self.button["kill"] = QPushButton('Zabij')

        # napis
        self.min_temp_value = QLabel(str(0), self)
        self.max_temp_value = QLabel(str(float('inf')), self)


        #ustawienia
        for key in self.editlines:
            self.editlines[key].setMaximumWidth(self.width_editline)

        self.editlines['calls'].setText(str(self.wywolanie.calls_parameters['ilosc_wywolan']))
        self.editlines['meridian_amount'].setText(str(self.wywolanie.calls_parameters['ilosc_poludnikow']))
        self.editlines['parallel_amount'].setText(str(self.wywolanie.calls_parameters['ilosc_rownoleznikow']))
        self.editlines['albedo_land'].setText(str(self.wywolanie.calls_parameters['albedo_parametr_lad']))
        self.editlines['albedo_sea'].setText(str(self.wywolanie.calls_parameters['albedo_parametr_morze']))
        self.editlines['coof_reemision'].setText(str(self.wywolanie.calls_parameters['wspulczynnik_reemisji']))
        self.editlines['coof_dyfusion'].setText(str(self.wywolanie.calls_parameters['wsp_dyf']))
        self.editlines['sun_const'].setText(str(self.wywolanie.calls_parameters['stala_sloneczna']))

        self.sun.setChecked(True)
        self.emision.setChecked(True)
        self.heat.setChecked(True)

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

        min_temp_l = [
            ('widget', QLabel('temp min:', self)),
            ('widget', self.min_temp_value),
        ]

        max_temp_l = [
            ('widget', QLabel('temp max:', self)),
            ('widget', self.max_temp_value),
        ]

        self.min_temp_box = self.box('horizontal', min_temp_l)
        self.max_temp_box = self.box('horizontal', max_temp_l)



        side_bar_l = [
        # radio button
            ('widget', self.sun),
            ('widget', self.emision),
            ('widget', self.heat),

        # editline
            ('widget', QLabel('ilość wywołań', self)),
            ('widget', self.editlines['calls']),
            ('widget', QLabel('ilość południków', self)),
            ('widget', self.editlines['meridian_amount']),
            ('widget', QLabel('ilość równoleżników', self)),
            ('widget', self.editlines['parallel_amount']),
            ('widget', QLabel('współczynnik albedo dla lądu', self)),
            ('widget', self.editlines['albedo_land']),
            ('widget', QLabel('współczynnik albedo dla morza', self)),
            ('widget', self.editlines['albedo_sea']),
            ('widget', QLabel('współczynnik reemisji', self)),
            ('widget', self.editlines['coof_reemision']),
            ('widget', QLabel('współczynnik dyfuzji', self)),
            ('widget', self.editlines['coof_dyfusion']),
            ('widget', QLabel('stała słoneczna', self)),
            ('widget', self.editlines['sun_const']),

        # labels
            #('widget', self.meridian_amount),
            #('widget', self.parallel_amount),
            ('widget', self.time),
            ('layout', self.min_temp_box),
            ('layout', self.max_temp_box),
            ('widget', self.button["generate"]),
            ('widget', self.button["kill"]),
            ('stretch',),
        ]

        self.side_bar_box = self.box('vertical', side_bar_l)


        print('side bar width:', self.side_bar_box.contentsRect().width())


        #self.width_map = 800
        #self.height_map = self.width_map/5

        map_hl = [
            ('stretch',),
            ('widget', self.map_item),
            ('stretch',),
        ]

        self.map_hbox = self.box('horizontal', map_hl)

        map_vl = [
            ('stretch',),
            ('layout', self.map_hbox),
            ('stretch',),
        ]

        self.map_vbox = self.box('vertical', map_vl)

        bottom_l = [
            ('layout', self.map_vbox),
            ('layout', self.side_bar_box),
        ]

        self.bottom_box = self.box('horizontal', bottom_l)

        main_l = [
            ('layout', self.header_box),
            ('layout', self.bottom_box),
        ]

        self.mainbox = self.box('vertical', main_l)

        #podpiecie przyciskow
        slots = {
            'generate': self.generate,
            'kill': QtCore.QCoreApplication.instance().quit,
            }

        self.slot_conn(slots)
        self.setLayout(self.mainbox)
        self.show()

        # ustawienie rozmiaru labela mapy
        self.width_map = self.screen_size()['w'] - self.side_bar_box.contentsRect().width()*1.5
        self.height_map = self.width_map/2
        self.set_map_label_size()

    # definicja podpiec
    def slot_conn(self, slots={}):
        for key in slots:
            self.button[key].clicked.connect(slots[key])
            print(">checkpoint: slots plugging for key: ", key, 'in class: ', self.__class__.__name__)

    # definicje funkcji podpinanych do przyciskow
    def generate(self):
        self.generate_map()
        """
        self.map.pixel[5][5] = qRgb(0, 0, 0)
        self.map.map.setPixel(5, 5, self.map.pixel[5][5])
        self.map_item.setPixmap(QPixmap.fromImage(self.map.map))
        """
        print('generuje')

    def kill(self):
        print('morduje')
        self.main.stacked_widget.removeWidget(self.main.stacked_widget.currentWidget())

    # pomocnicza metoda do budowania layout'u
    def box(self, el_type, elems):

        if el_type == 'vertical':
            box = QtGui.QVBoxLayout()

        elif el_type == 'horizontal':
            box = QtGui.QHBoxLayout()

        for elem in elems:
            if elem[0] == 'stretch':
                    box.addStretch(1)
            elif elem[1] is not None:
                if elem[0] == 'widget':
                    box.addWidget(elem[1])
                elif elem[0] == 'layout':
                    box.addLayout(elem[1])

        return box

    def temp_to_rgb(self):
        self.rgb = []
        for row in self.map_data.map_data:
            row_rgb = []
            for item in row:

                if item < self.min_temp and item > 1:
                    self.min_temp = item
                if item > self.max_temp:
                    self.max_temp = item

                item_rgb = {}
                item_rgb['r'] = item
                item_rgb['g'] = item
                item_rgb['b'] = item
                row_rgb.append(item_rgb)
            self.rgb.append(row_rgb)

    def generate_map(self):
        print('doing nothing')

        # definiowanie parametrow
        calls_temp = self.editlines['calls'].text()
        if calls_temp != '':
            self.wywolanie.calls_parameters['ilosc_wywolan'] = calls_temp


        meridian_amount_temp = self.editlines['meridian_amount'].text()
        if meridian_amount_temp != '':
            self.wywolanie.calls_parameters['ilosc_poludnikow'] = meridian_amount_temp

        parallel_amount_temp = self.editlines['parallel_amount'].text()
        if parallel_amount_temp != '':
            self.wywolanie.calls_parameters['ilosc_rownoleznikow'] = parallel_amount_temp

        albedo_sea_temp = self.editlines['albedo_sea'].text()
        if albedo_sea_temp != '':
            self.wywolanie.calls_parameters['albedo_parametr_morze'] = albedo_sea_temp

        albedo_land_temp = self.editlines['albedo_land'].text()
        if albedo_land_temp != '':
            self.wywolanie.calls_parameters['albedo_parametr_lad'] = albedo_land_temp

        coof_reem = self.editlines['coof_reemision'].text()
        if coof_reem != '':
            self.wywolanie.calls_parameters['wspulczynnik_reemisji'] = coof_reem

        coof_dyf = self.editlines['coof_dyfusion'].text()
        if coof_dyf != '':
            self.wywolanie.calls_parameters['wsp_dyf'] = coof_dyf

        sun_const = self.editlines['sun_const'].text()
        if sun_const != '':
            self.wywolanie.calls_parameters['stala_sloneczna'] = sun_const

        sun = self.sun.isChecked()
        emis = self.emision.isChecked()
        heat = self.heat.isChecked()

        if sun:
            self.wywolanie.calls_parameters['fun_slonce'] = 1
        else:
            self.wywolanie.calls_parameters['fun_slonce'] = 0

        if emis:
            self.wywolanie.calls_parameters['fun_emisja'] = 1
        else:
            self.wywolanie.calls_parameters['fun_emisja'] = 0

        if heat:
            self.wywolanie.calls_parameters['fun_wymiana_ciepla'] = 1
        else:
            self.wywolanie.calls_parameters['fun_wymiana_ciepla'] = 0



        self.wywolanie.run()

        # # odczyt pliku
        self.map_data = None
        self.map_data = DataStorage('../../wersja6/temperatura_0.txt')
        self.x = self.map_data.rows
        self.y = self.map_data.columns

        print('x map', self.x)
        print('y map', self.y)

        self.min_temp = float('inf')
        self.max_temp = 0

        map_old = self.map
        self.map = Map(self.x, self.y)
        #del map_old
        self.temp_to_rgb()

        print('rgb:\n', self.rgb)

        #zmieniam recznie max, min
        #self.min_temp = 300
        #self.max_temp = 400

        # # definicja obrazu mapy
        self.range_temp = self.max_temp-self.min_temp

        print('x rgb', len(self.rgb))
        print('y rgb', len(self.rgb[0]))

        self.map.init_pixels(self.rgb, self.min_temp, self.range_temp)

        # # nalozenie obrazu na mape
        self.map.set_pixels()

        # # przypiecie obrazu
        self.map_item.setPixmap(QPixmap.fromImage(self.map.map))

        # # ustawianie napisow
        self.min_temp_value.setText(str(int(self.min_temp-273.15)))
        self.max_temp_value.setText(str(int(self.max_temp-273.15)))

    def screen_size(self):
        rec = QApplication.desktop().screenGeometry()
        height = rec.height()
        width = rec.width()
        return {'w': width, 'h': height}

    def set_map_label_size(self):
        w = self.width_map
        h = self.height_map
        self.map_item.setMaximumWidth(w)
        self.map_item.setMaximumHeight(h)
        self.map_item.setMinimumWidth(w)
        self.map_item.setMinimumHeight(h)