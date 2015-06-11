__author__ = 'mcmushroom'
import os, sys
from check_system import check_system

class DataStorage:

    def __init__(self, path_data):

        self.path = path_data
        self.map_data = []
        
        self.decode_to_dict()

        self.rows = len(self.map_data)
        self.columns = len(self.map_data[0])

    def decode_to_dict(self):
        self.map_data = []
        n = 1
        for data_row in open(self.path, 'r').read().split('\n'):
            if data_row != '':
                temp_tab = []
                for data_item in data_row.split(' '):
                    if data_item != '':
                        temp_tab.append(float(data_item))
                self.map_data.append(temp_tab)


class Paths:
    def __init__(self, main_project_folder_name):
        self.path = {
            'calls': None,
            'models': None,
            'simulator': None,
            'simulator_win': None,
            'views': None,
            'master': None,
            }

        current_path = os.getcwd()

        print('path in class Paths:', current_path)

        levels = None
        slash = None
        project_path = False
        if check_system() == 'linux':
            slash = '/'
        elif check_system() == 'windows':
            slash = '\\'

        levels = current_path.split(slash)
        print('level in path from class Paths:', levels)

        #print('is?:',  levels[-2] == main_project_folder_name)
        for level in reversed(levels):
            if level == main_project_folder_name:
                project_path = ''
                for level in levels:
                    project_path += level + slash
                for key in self.path:
                    self.path[key] = project_path + key + slash
                break
            else:
                del levels[-1]

        print('main project folder path is:\n', project_path)


if __name__ == '__main__':
    main_path = Paths('apka')
    for key in main_path.path:
        print(key, '--', main_path.path[key])

