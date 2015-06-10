__author__ = 'mcmushroom'
import os

def project_path():
    return os.getcwd()

if __name__ == '__main__':
    print('Ścieżka głównego folderu projektu:')
    print(project_path())