__author__ = 'mcmushroom'

from PyQt4 import QtCore, QtGui
from view.main_view import MainWindow


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        #tworzenie stosu widokow
        self.stacked_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        #zaladowanie glownego okna
        main_window = MainWindow()
        self.setWindowIcon(QtGui.QIcon('../image/app_ico.png'))
        self.setWindowTitle('World albedo')
        self.resize(800, 600)
        self.center()
        self.stacked_widget.addWidget(main_window)

        #podpiecie przyciskow
        slots = {}

        main_window.slot_conn(slots)

    #definicje funkcji podpinanych do przyciskow

    #definicja wysrodkowania okna
    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = Main()
    window.show()
    app.exec_()


