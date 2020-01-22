#!/usr/bin/env python2
import sys
from hr_payEl import append_hr_payEl

class Dictionary:
    def __init__(self, src_path, dst_path):
        self.TaxCode = {}
        self.PayElID = {}
        self.error_count = 0
        self.src_path = src_path
        self.dst_path = dst_path

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
            ID = self.PayElID.len + 1                    
            ID = append_hr_payEl(ID, cd, cd, self.src_path, self.dst_path)
            if (ID == 0):
                self.error_count += 1
                print '[' + str(self.error_count) + '] Not found PayElCd: ' + cd + '.'
            else:
                self.set_PayElID(cd, ID)
            return ID
