__author__ = 'mcmushroom'

from subprocess import call
import os
import subprocess
import time
from models.data_storage import Paths
from check_system import check_system
import re


class Calling:
    def __init__(self, path_to_simulator, view, main):

        self.main = main
        self.view = view
        self.system = check_system()

        self.year = view.year_value
        self.day = view.day_value
        self.time = view.time_value

        self.avr_temp = view.avr_temp_value
        self.min_temp = view.min_temp_value
        self.max_temp = view.max_temp_value
        self.avr_albedo = view.avr_albedo_value

        self.path = Paths('apka')

        self.calls_parameters = {
            'path': path_to_simulator,
            'ilosc_poludnikow': 100,
            'ilosc_rownoleznikow': 100,
            'stala_sloneczna': 1300,
            'wspulczynnik_reemisji': 0.52,
            'wsp_dyf': 300,
            'fun_slonce': 1,
            'fun_emisja': 1,
            'fun_wymiana_ciepla': 1,
            'albedo_parametr_lad': 0.34,
            'albedo_parametr_morze': 0.27,
            'albedo_rodzaj': 0,
            'ilosc_wywolan': 200,
            'cieplo_wlasciwe_lad': 100000,
            'cieplo_wlasciwe_morze': 300000,
            'czyt_mape_swiata': 1,
        }

        if self.system == 'linux':
            self.calls_parameters['path'] = fix_path(self.calls_parameters['path'])
        print('>fix path:', self.calls_parameters['path'])

    #wywolanie symulatora na podstawie skryptu

    # def run(self):
    #     #zdefiniowanie komendy wywolania
    #     calling = ''
    #     #calling += 'pwd' + '\n'
    #     calling += 'cd '
    #     if self.system == 'linux':
    #         calling += self.calls_parameters['path'] + '\n'
    #     elif self.system == 'windows':
    #         calling += '"' + self.calls_parameters['path'] + '"' + '\n'
    #     #calling += 'pwd' + '\n'
    #     if self.system == 'linux':
    #         calling += './main '
    #     elif self.system == 'windows':
    #         calling += 'main_wojtek.exe '
    #     calling += str(self.calls_parameters['ilosc_poludnikow']) + ' '
    #     calling += str(self.calls_parameters['ilosc_rownoleznikow']) + ' '
    #     calling += str(self.calls_parameters['stala_sloneczna']) + ' '
    #     calling += str(self.calls_parameters['wspulczynnik_reemisji']) + ' '
    #     calling += str(self.calls_parameters['wsp_dyf']) + ' '
    #     calling += str(self.calls_parameters['fun_slonce']) + ' '
    #     calling += str(self.calls_parameters['fun_emisja']) + ' '
    #     calling += str(self.calls_parameters['fun_wymiana_ciepla']) + ' '
    #     calling += str(self.calls_parameters['albedo_parametr_lad']) + ' '
    #     calling += str(self.calls_parameters['albedo_parametr_morze']) + ' '
    #     calling += str(self.calls_parameters['albedo_rodzaj']) + ' '
    #     calling += str(self.calls_parameters['ilosc_wywolan']) + ' '
    #     calling += str(self.calls_parameters['cieplo_wlasciwe_lad']) + ' '
    #     calling += str(self.calls_parameters['cieplo_wlasciwe_morze']) + ' '
    #     calling += str(self.calls_parameters['czyt_mape_swiata'])
    #
    #     print('>calling:\n\n', calling, '\n')
    #
    #     #przeniesienie komendy wywolania do skryptu
    #     if self.system == 'linux':
    #         print('>file path:', self.path.path['simulator']+'calling.sh')
    #         open(self.path.path['simulator']+'calling.sh', 'w').write("#!/bin/bash\n\n"+calling)
    #     elif self.system == 'windows':
    #         print('>file path:', self.path.path['simulator_win']+'calling.bat')
    #         open(self.path.path['simulator_win']+'calling.bat', 'w').write(calling)
    #
    #     #print('>execute ls -l\n')
    #     #execute(['ls', '-l'])
    #
    #     #print('\n>execute pwd\n')
    #     #execute(['pwd'])
    #
    #     #wywolanie skryptu z komenda
    #     if self.system == 'linux':
    #         print('\n>execute calling.sh\n')
    #         print(open(self.path.path['simulator']+'calling.sh', 'r').read())
    #         self.execute([self.path.path['simulator']+'calling.sh'])
    #     elif self.system == 'windows':
    #         print('\n>execute calling.bat\n')
    #         print(open(self.path.path['simulator_win']+'calling.bat', 'r').read())
    #         self.execute([self.path.path['simulator_win']+'calling.bat'])

    #wywolanie komendy bezposrednio
    def run(self):
        calling = [
            self.calls_parameters['path']+'main_wojtek.exe',
            str(self.calls_parameters['ilosc_poludnikow']),
            str(self.calls_parameters['ilosc_rownoleznikow']),
            str(self.calls_parameters['stala_sloneczna']),
            str(self.calls_parameters['wspulczynnik_reemisji']),
            str(self.calls_parameters['wsp_dyf']),
            str(self.calls_parameters['fun_slonce']),
            str(self.calls_parameters['fun_emisja']),
            str(self.calls_parameters['fun_wymiana_ciepla']),
            str(self.calls_parameters['albedo_parametr_lad']),
            str(self.calls_parameters['albedo_parametr_morze']),
            str(self.calls_parameters['albedo_rodzaj']),
            str(self.calls_parameters['ilosc_wywolan']),
            str(self.calls_parameters['cieplo_wlasciwe_lad']),
            str(self.calls_parameters['cieplo_wlasciwe_morze']),
        ]
        print('calling: ', calling)

        simulator_process = subprocess.Popen(calling)
        while interpreter(simulator_process.stdout):
            pass


    # def execute(self, command):
    #     popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    #     lines_iterator = iter(popen.stdout.readline, b"")
    #     for line in lines_iterator:
    #         print('line:', line) # yield line
    #         set_from_cout('avr_temp', str(line), self.avr_temp)
    #         set_from_cout('min_temp', str(line), self.min_temp)
    #         set_from_cout('max_temp', str(line), self.max_temp)
    #         set_from_cout('avr_albe', str(line), self.avr_albedo)
    #         set_from_cout('year', str(line), self.year)
    #         set_from_cout('day', str(line), self.day)
    #         set_from_cout('time', str(line), self.time)
    #
    #
    #
    #
    #
    #         status = get_from_cout('status', str(line))
    #         if status is not None and status is not False:
    #             print('status', status)
    #
    #             self.main.statusBar().showMessage(str(status))


def interpreter(stdout):
    import time
    time.sleep(1)
    print('<stdout>: ', stdout, '</stdout>')
    return True

def fix_path(path):
    return path.replace(' ', '\ ')


def set_from_cout(tag, line, label):
    expression = re.compile(".*<%s>(?P<value>.+)</%s>.*$" % (tag, tag))
    m = expression.match(line)
    if m:
        label.setText(str(m.group('value')))


def get_from_cout(tag, line):
    expression = re.compile(".*<%s>(?P<value>.+)</%s>.*$" % (tag, tag))
    m = expression.match(line)
    if m:
        return m.group('value')


if __name__ == '__main__':
    exit(0)





