__author__ = 'mcmushroom'
import os, sys

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


class Paths():
    def __init__(self, main_project_folder_name):
        self.path = {
            'calls': None,
            'models': None,
            'simulator': None,
            'views': None,
            'master': None,
            }

        current_path = os.getcwd()
        project_path = False
        levels = current_path.split('/')
        #print('is?:',  levels[-2] == main_project_folder_name)
        for level in reversed(levels):
            if level == main_project_folder_name:
                project_path = ''
                for level in levels:
                    project_path += level + '/'
                for key in self.path:
                    self.path[key] = project_path + key + '/'
                break
            else:
                del levels[-1]

        print('main project folder path is:\n', project_path)


if __name__ == '__main__':
    main_path = Paths('apka')
    for key in main_path.path:
        print(key, '--', main_path.path[key])

