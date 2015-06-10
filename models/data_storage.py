__author__ = 'mcmushroom'

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