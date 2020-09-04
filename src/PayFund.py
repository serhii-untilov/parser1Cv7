#!/usr/bin/env python2
import sys


class PayFund:
    def __init__(self):
        self.ID = 0
        self.code = ''
        self.name = ''

    def write_header(self, f):
        f.write('ID;code;name\n')

    def write_record(self, f):
        f.write('%d;%s;%s\n' % (self.ID, self.code, self.name))
