#!/usr/bin/env python2
import sys
from src.PayEl import PayEl
from sets import Set

class Dictionary:
    def __init__(self, src_path, dst_path):
        self.TaxCode = {}
        self.PayElID = {}
        self.DepartmentID = {}
        self.DictPositionName = {}
        self.PayElCode = Set()
        self.error_count = 0
        self.src_path = src_path
        self.dst_path = dst_path

    def setPayElCode(self, code): 
        if (code not in self.PayElCode):
            self.PayElCode.add(code)

    def getPayElCode(self, code): 
        return (code in self.PayElCode)

    def set_DepartmentID(self, code, ID):
        self.DepartmentID[code] = ID

    def get_DepartmentID(self, code):
        try:
            return self.DepartmentID[code] and self.DepartmentID[code] or ''
        except:
            self.error_count += 1
            print 'Error [' + str(self.error_count) + ']. Not found Department code: ' + code + '.'
            return ''

    def set_DictPositionName(self, code, name):
        self.DictPositionName[code] = name

    def get_DictPositionName(self, code):
        try:
            return self.DictPositionName[code] and self.DictPositionName[code] or ''
        except:
            self.error_count += 1
            print 'Error [' + str(self.error_count) + ']. Not found dictPosition code: ' + code + '.'
            return ''


    def set_TaxCode(self, tabNum, taxCode):
        self.TaxCode[tabNum] = taxCode

    def get_TaxCode(self, tabNum):
        try:
            return self.TaxCode[tabNum] and self.TaxCode[tabNum] or ''
        except:
            self.error_count += 1
            print 'Error [' + str(self.error_count) + ']. Not found tabNum: ' + tabNum + '.'
            return ''

    def set_PayElID(self, cd, payElID):
        self.PayElID[cd] = payElID

    def get_PayElID(self, cd):
        code = str(cd)[:32]
        try:
            return self.PayElID[code] and self.PayElID[code] or 0
        except:
            ID = len(self.PayElID) + 1                    
            ID = _append_hr_payEl(ID, code, code, self.src_path, self.dst_path)
            if (ID == 0):
                self.error_count += 1
                print 'Error [' + str(self.error_count) + ']. Not found PayElCd: ' + cd + '.'
            else:
                self.set_PayElID(code, ID)
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
        print 'Not added', dst_file, sys.exc_info()[1]
        return 0
