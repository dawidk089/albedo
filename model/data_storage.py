__author__ = 'mcmushroom'


class DataStorage:

    def __init__(self, path_data):
        self.path = path_data
        self.data_dic = {}
        
        self.decode_to_dict()

        self.ilosc_rownoleznikow = 0
        self.ilosc_poludnikow = len(self.data_dic)

        self.valid = True
        first = False
        for key in self.data_dic:
            if not first:
                first = True
                self.ilosc_rownoleznikow = len(self.data_dic[key])
            else:
                if self.ilosc_rownoleznikow != len(self.data_dic[key]):
                    self.valid = False

    def decode_to_dict(self):
        is_poludnik = []
        for data_row in open(self.path, 'r').read().split('x'):
            data_list_row = data_row.split(' ')
            if data_row != "":
                poludnik = data_list_row[1]
                rownoleznik = data_list_row[2]

                temp_dic = {
                    'temperatura': data_list_row[3],
                    'ref_nr_poludnik': data_list_row[4],
                    'ref_nr_rownoleznik': data_list_row[5],
                    'ref_dlugosc_poludnikowa': data_list_row[6],
                    'ref_dlugosc_rownoleznikowa': data_list_row[7],
                    'ref_pole_powierzchni': data_list_row[8],
                    'ref_albedo': data_list_row[9],
                    'ref_cieplo_wlasciwe': data_list_row[10],
                    'ref_wspolczynnik_dyfuzji': data_list_row[11],
                    'ref_energia_wew': data_list_row[12],
                }

                if poludnik not in self.data_dic:
                    self.data_dic[poludnik] = []
                self.data_dic[poludnik].append({rownoleznik: temp_dic})

if __name__ == '__main__':
    decode = DataStorage('plik_zapisu.txt')

    print('ilosc poludnikow: ', decode.ilosc_poludnikow)
    print('ilosc rownoleznikow: ', decode.ilosc_rownoleznikow)
    print('czy poprawne: ', decode.valid)


