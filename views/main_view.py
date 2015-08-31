# -*- coding: utf-8 -*-
__author__ = 'mcmushroom'

from PyQt4 import QtGui, QtCore
from models.map import Map
from models.data_storage import DataStorage
from calls.calling import Calling
from check_system import check_system


class MainWindow(QtGui.QWidget):

    def __init__(self, main, path):
        super(MainWindow, self).__init__()

        print('>start init main_view')

        self.main = main
        self.path = path

        # init sets
        self.width_editline = 100
        
        # naglowek
        self.header = QtGui.QLabel('<h1><b>Albedo Ziemi</b></h1>', self)

        # # zadeklarowanie wymiarow mapy
        #self.map = Map(self.x, self.y)
        self.map = Map(600, 800)

        # # definicja tablicy rgb
        self.rgb = []
        self.map.init_pixels0()

        # # nalozenie obrazu na mape
        self.map.set_pixels()

        self.map_item = QtGui.QLabel()

        self.width_map = self.screen_size()['w']-self.width_editline
        self.height_map = self.screen_size()['h']*self.width_editline

        self.map_item.setScaledContents(True)
        self.map_item.setPixmap(QtGui.QPixmap.fromImage(self.map.map))

        # check button
        self.sun = QtGui.QCheckBox('słońce')
        self.emision = QtGui.QCheckBox('emisja')
        self.heat = QtGui.QCheckBox('przewodnictwo')
        #self.const_albedo = QtGui.QCheckBox('rodzaj albedo')
        self.map_world = QtGui.QCheckBox('wczytanie poprzedniej mapy')

        self.albedo_mode = QtGui.QComboBox()

        # editline
        self.editlines = {
            'calls': QtGui.QLineEdit(self),
            'albedo_land': QtGui.QLineEdit(self),
            'albedo_sea': QtGui.QLineEdit(self),
            'coof_reemision': QtGui.QLineEdit(self),
            'coof_dyfusion': QtGui.QLineEdit(self),
            'sun_const': QtGui.QLineEdit(self),
            'meridian_amount': QtGui.QLineEdit(self),
            'parallel_amount': QtGui.QLineEdit(self),
            'land_specific_heat': QtGui.QLineEdit(self),
            'sea_specific_heat': QtGui.QLineEdit(self),
        }

        # labels
        #self.meridian_amount = QLabel('ilość południków: '+str(0), self)
        #self.parallel_amount = QLabel('ilość równoleżników: '+str(0), self)
        #self.time = QtGui.QLabel('czas: '+str(0), self)

        # button
        self.button = {}

        self.button["generate"] = QtGui.QPushButton('Generuj')
        self.button["kill"] = QtGui.QPushButton('Zabij')
        self.button["test"] = QtGui.QPushButton('Testuj')

        # napis
        self.min_temp_value = QtGui.QLabel(str('n/a'), self)
        self.max_temp_value = QtGui.QLabel(str('n/a'), self)
        self.avr_temp_value = QtGui.QLabel(str('n/a'), self)
        self.avr_albedo_value = QtGui.QLabel(str('n/a'), self)
        #TODO temperatury dac na wyswietlanie w okienku

        self.year_value = QtGui.QLabel(str('n/a'), self)
        self.day_value = QtGui.QLabel(str('n/a'), self)
        self.time_value = QtGui.QLabel(str('n/a'), self)

        # utworzenie obiektu pod wywolanie symulatora
        if check_system() == 'linux':
            self.wywolanie = Calling(self.path.path['simulator'], self, self.main)
        elif check_system() == 'windows':
            self.wywolanie = Calling(self.path.path['simulator_win'], self, self.main)

        #ustawienia
        self.albedo_mode.setEditable(True)
        self.albedo_mode.addItems(['1', '2', '3', '4'])
        self.albedo_mode.setMaximumWidth(100)


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
        self.editlines['land_specific_heat'].setText(str(self.wywolanie.calls_parameters['cieplo_wlasciwe_lad']))
        self.editlines['sea_specific_heat'].setText(str(self.wywolanie.calls_parameters['cieplo_wlasciwe_morze']))

        self.sun.setChecked(True)
        self.emision.setChecked(True)
        self.heat.setChecked(True)
        #self.const_albedo.setChecked(True)
        self.map_world.setChecked(True)

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
            ('widget', QtGui.QLabel('temp min:', self)),
            ('widget', self.min_temp_value),
        ]

        max_temp_l = [
            ('widget', QtGui.QLabel('temp maks:', self)),
            ('widget', self.max_temp_value),
        ]

        avr_temp_l = [
            ('widget', QtGui.QLabel('temp śr.:', self)),
            ('widget', self.avr_temp_value),
        ]

        avr_albedo_l = [
            ('widget', QtGui.QLabel('albedo śr.:', self)),
            ('widget', self.avr_albedo_value),
            ('widget', self.albedo_mode)
        ]

        time_l = [
            ('widget', QtGui.QLabel('czas', self)),
            ('widget', self.year_value),
            ('widget', QtGui.QLabel('rok,', self)),
            ('widget', self.day_value),
            ('widget', QtGui.QLabel('dzień,:', self)),
            ('widget', self.time_value),
            ]

        self.min_temp_box = self.box('horizontal', min_temp_l)
        self.max_temp_box = self.box('horizontal', max_temp_l)
        self.avr_temp_box = self.box('horizontal', avr_temp_l)
        self.avr_albedo_box = self.box('horizontal', avr_albedo_l)
        self.time_box = self.box('horizontal', time_l)


        side_bar_l = [

            ('stretch',),

        # editline
            ('widget', QtGui.QLabel('ilość południków', self)),
            ('widget', self.editlines['meridian_amount']),
            ('widget', QtGui.QLabel('ilość równoleżników', self)),
            ('widget', self.editlines['parallel_amount']),
            ('widget', QtGui.QLabel('stała słoneczna', self)),
            ('widget', self.editlines['sun_const']),
            ('widget', QtGui.QLabel('współczynnik reemisji', self)),
            ('widget', self.editlines['coof_reemision']),
            ('widget', QtGui.QLabel('współczynnik dyfuzji', self)),
            ('widget', self.editlines['coof_dyfusion']),

            ('stretch',),

        # radio button
            ('widget', self.sun),
            ('widget', self.emision),
            ('widget', self.heat),

            ('stretch',),

        # editline (continued)
            ('widget', QtGui.QLabel('współczynnik albedo dla lądu', self)),
            ('widget', self.editlines['albedo_land']),
            ('widget', QtGui.QLabel('współczynnik albedo dla morza', self)),
            ('widget', self.editlines['albedo_sea']),
            #TODO rodzaj albedo
            #('widget', self.const_albedo),

            ('widget', QtGui.QLabel('ilość wywołań', self)),
            ('widget', self.editlines['calls']),
            #TODO cieplo wlasciwe ladu
            ('widget', QtGui.QLabel('ciepło właściwe lądu', self)),
            ('widget', self.editlines['land_specific_heat']),
            #TODO cieplo wlasciwe morza
            ('widget', QtGui.QLabel('ciepło właściwe morza', self)),
            ('widget', self.editlines['sea_specific_heat']),
            #TODO czyt_mape_swiata
            ('widget', self.map_world),
            ('widget', QtGui.QLabel('rodzaj albedo', self)),
            ('widget', self.albedo_mode),


            ('stretch',),

        # labels
            #('widget', self.meridian_amount),
            #('widget', self.parallel_amount),
            ('layout', self.min_temp_box),
            ('layout', self.max_temp_box),
            ('layout', self.avr_temp_box),
            ('layout', self.avr_albedo_box),
            ('layout', self.time_box),

            ('stretch',),

        # button
            ('widget', self.button["generate"]),
            ('widget', self.button["kill"]),
            #('widget', self.button["test"]),
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
            'test': self.test,
            'kill': QtCore.QCoreApplication.instance().quit,
            }

        self.slot_conn(slots)
        self.setLayout(self.mainbox)
        self.show()

        self.main.statusBar().showMessage('Symulator w stanie gotowości.')

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
        self.main.statusBar().showMessage('Trwają symulacje...')
        self.generate_map()
        self.main.statusBar().showMessage('Symulator jest w stanie gotowości.')
        print('generuje')

    def kill(self):
        print('morduje')
        #print(self.albedo_mode.itemData(self.albedo_mode.currentIndex()))
        self.main.stacked_widget.removeWidget(self.main.stacked_widget.currentWidget())

    def test(self):
        #print(self.albedo_mode.itemData(self.albedo_mode.currentIndex()))
        print(self.albedo_mode.currentText())
        #print('test przycisku test')

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

                if item < self.min_temp:
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
        #c_albedo = self.const_albedo.isChecked()
        world = self.map_world.isChecked()


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

        albedo_mode = self.albedo_mode.currentText()

        if albedo_mode == '1':
            self.wywolanie.calls_parameters['albedo_rodzaj'] = 1
        elif albedo_mode == '2':
            self.wywolanie.calls_parameters['albedo_rodzaj'] = 2
        elif albedo_mode == '3':
            self.wywolanie.calls_parameters['albedo_rodzaj'] = 3
        elif albedo_mode == '4':
            self.wywolanie.calls_parameters['albedo_rodzaj'] = 4
        else:
            print('zadne albedo_mode nie zostalo wybrane')

        # if c_albedo:
        #     self.wywolanie.calls_parameters['albedo_rodzaj'] = 1
        # else:
        #     self.wywolanie.calls_parameters['albedo_rodzaj'] = 0

        if world:
            self.wywolanie.calls_parameters['czyt_mape_swiata'] = 1
        else:
            self.wywolanie.calls_parameters['czyt_mape_swiata'] = 0

        self.wywolanie.run()

        #tymczasowo przerwanie funkcji
        return

        # tutaj ustawianie wartosci

        # # odczyt pliku
        self.map_data = None
        if check_system() == 'linux':
            self.map_data = DataStorage(self.path.path['simulator'] + 'temperatura_0.txt')
        elif check_system() == 'windows':
           self.map_data = DataStorage(self.path.path['simulator_win'] + 'temperatura_0.txt')

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

        #print('rgb:\n', self.rgb)

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
        self.map_item.setPixmap(QtGui.QPixmap.fromImage(self.map.map))

        # # ustawianie napisow
        #self.min_temp_value.setText(str(int(self.min_temp-273.15)))
        #self.max_temp_value.setText(str(int(self.max_temp-273.15)))

    def screen_size(self):
        rec = QtGui.QApplication.desktop().screenGeometry()
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
