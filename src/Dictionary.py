#!/usr/bin/env python2
import sys

class Dictionary:
    def __init__(self):
        self.TaxCode = {}
        self.PayElID = {}
        self.error_count = 0

    def set_TaxCode(self, tabNum, taxCode):
        self.TaxCode[tabNum] = taxCode

    def get_TaxCode(self, tabNum):
        try:
            return self.TaxCode[tabNum] and self.TaxCode[tabNum] or ''
        except:
            self.error_count += 1
            print '[' + str(self.error_count) + '] Not found tabNum: ' + tabNum + '.'
            return ''

    def set_PayElID(self, cd, payElID):
        self.PayElID[cd] = payElID

    def get_PayElID(self, cd):
        try:
            return self.PayElID[cd] and self.PayElID[cd] or 0
        except:
            self.error_count += 1
            print '[' + str(self.error_count) + '] Not found PayElCd: ' + cd + '.'
            return 0
