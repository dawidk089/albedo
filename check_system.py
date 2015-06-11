__author__ = 'mcmushroom'

def check_system():
    from sys import platform as _platform
    if _platform == "linux" or _platform == "linux2":
        return 'linux'
    elif _platform == "win32":
        return 'windows'