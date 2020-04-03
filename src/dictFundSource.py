#!/usr/bin/env python2
import sys


class DictFundSource:
    def __init__(self):
        self.ID = 0
        self.code = 0
        self.name = ''

    def write_header(self, f):
        f.write('ID;code;name\n')

    def write_record(self, f):
        f.write('{};{};{}\n'.format(self.ID, self.code, self.name))
