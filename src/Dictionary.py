#!/usr/bin/env python2
import sys
from src.PayEl import PayEl


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
            ID = len(self.PayElID) + 1                    
            ID = _append_hr_payEl(ID, cd, cd, self.src_path, self.dst_path)
            if (ID == 0):
                self.error_count += 1
                print '[' + str(self.error_count) + '] Not found PayElCd: ' + cd + '.'
            else:
                self.set_PayElID(cd, ID)
            return ID

def _append_hr_payEl(ID, code, name, src_path, dst_path):
    dst_file = dst_path + 'hr_payEl.csv'
    try:
        f = open(dst_file, 'a+')
        payEl = PayEl()
        payEl.ID = ID
        payEl.code = code
        payEl.name = name
        payEl.description = payEl.name + '(' + payEl.code + ')'
        payEl.write_record(f)
        print 'Append', dst_file, ID, code, name
        return ID
    except:
        print 'Error append ', dst_file, sys.exc_info()[1]
        return 0
