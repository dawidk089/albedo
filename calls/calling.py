__author__ = 'mcmushroom'

from subprocess import call
import os
import subprocess
import time


class Calling:
    def __init__(self, path):

        self.calls_parameters = {
            'path': path,
            'ilosc_poludnikow': 100,
            'ilosc_rownoleznikow': 100,
            'stala_sloneczna': 1300,
            'wspulczynnik_reemisji': 0.8,
            'wsp_dyf': 0.5,
            'fun_slonce': 1,
            'fun_emisja': 1,
            'fun_wymiana_ciepla': 0,
            'albedo_parametr_lad': 0.2,
            'albedo_parametr_morze': 0.6,
            'albedo_rodzaj': 0,
            'ilosc_wywolan': 1000,
            'cieplo_wlasciwe_lad': 5000,
            'cieplo_wlasciwe_morze': 30000,
        }
        
    def run_and_go(self):
        calling = [
            'pwd',
            '&&',
            'cd',
            self.calls_parameters['path'],
            '&&',
            'pwd',
            '&&',
            './main',
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
        """
        self.process = subprocess.Popen(calling, stdout=subprocess.PIPE)
        for line in self.process.stdout.readlines():
            if line[0]=='-':
                print('line', line.split())
        """

    def run(self):
        calling = ''
        calling += 'pwd '
        calling += '&& '
        calling += 'cd '
        calling += self.calls_parameters['path']
        calling += ' && '
        calling += 'pwd '
        calling += '&& '
        calling += './main '
        calling += str(self.calls_parameters['ilosc_poludnikow']) + ' '
        calling += str(self.calls_parameters['ilosc_rownoleznikow']) + ' '
        calling += str(self.calls_parameters['stala_sloneczna']) + ' '
        calling += str(self.calls_parameters['wspulczynnik_reemisji']) + ' '
        calling += str(self.calls_parameters['wsp_dyf']) + ' '
        calling += str(self.calls_parameters['fun_slonce']) + ' '
        calling += str(self.calls_parameters['fun_emisja']) + ' '
        calling += str(self.calls_parameters['fun_wymiana_ciepla']) + ' '
        calling += str(self.calls_parameters['albedo_parametr_lad']) + ' '
        calling += str(self.calls_parameters['albedo_parametr_morze']) + ' '
        calling += str(self.calls_parameters['albedo_rodzaj']) + ' '
        calling += str(self.calls_parameters['ilosc_wywolan']) + ' '
        calling += str(self.calls_parameters['cieplo_wlasciwe_lad']) + ' '
        calling += str(self.calls_parameters['cieplo_wlasciwe_morze'])

        print('calling:', calling)
        open('calling.sh', 'w').write("#!/bin/bash\n\n"+calling)

        execute(['ls', '-l'])
        execute(['./calling.sh'])
        #execute()


        #execute(calling)
        #execute('./period.sh')
        #execute('pwd ')

def execute(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    lines_iterator = iter(popen.stdout.readline, b"")
    for line in lines_iterator:
        print('line:', line) # yield line



if __name__ == '__main__':
    symulator = Calling('../wersja6')
    symulator.run()





