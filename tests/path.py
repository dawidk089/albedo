__author__ = 'mcmushroom'

import re

re_section = re.compile('\[(?P<sec>\w+)\]')
re_command = re.compile(';.*')
re_value = re.compile('(?P<n>\w+) *= *(?P<val>.*)')


#T/F
def is_section(l):
    m = re_section.match(l)
    #print(m.group('sec'))
    return bool(m) if not m else m.group(0)


#F/nazwa
def is_command(l):
    m = re_command.match(l)
    return m


if __name__ == "__main__":
    c = '; blah'
    s = '[sec]'
    v = 'x = 7'

    for x in [c, s, v]:
        print(is_section(x))