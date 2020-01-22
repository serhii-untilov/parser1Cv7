#!/usr/bin/env python2
import sys
from dbfpy import dbf
from Dictionary import Dictionary

class PayEl:
    def __init__(self):
        self.ID = 0
        self.code = ''
        self.name = ''
        self.methodID = ''
        self.description = ''
        self.dateFrom = ''
        self.dateTo = ''
        self.roundUpTo = '2'
        self.isAutoCalc = '1'
        self.isRecalculate = '1'
        self.calcProportion = ''
        self.calcSumType = ''
        self.periodType = ''
        self.dictExperienceID = ''
        self.calcMounth = ''
        self.averageMethod = ''
        self.typePrepayment = ''
        self.prepaymentDay = ''
        self.dictFundSourceID = ''

    def write_header(self, f):
        f.write('ID;code;name;methodID;description;dateFrom;dateTo;roundUpTo;isAutoCalc;isRecalculate;calcProportion;' + 
            'calcSumType;periodType;dictExperienceID;calcMounth;averageMethod;typePrepayment;prepaymentDay;dictFundSourceID\n')

    def write_record(self, f):
        f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (
            self.ID, self.code, self.name, self.methodID, self.description, self.dateFrom, 
            self.dateTo, self.roundUpTo, self.isAutoCalc, self.isRecalculate, 
            self.calcProportion, self.calcSumType, self.periodType, self.dictExperienceID, 
            self.calcMounth, self.averageMethod, self.typePrepayment, self.prepaymentDay, 
            self.dictFundSourceID)
        )


def hr_payEl(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_payEl.csv'
    try:
        dataset = dbf.Dbf(src_path + 'VO.DBF')
        f = open(dst_file, 'w+')
        payEl = PayEl()
        payEl.write_header(f)
        payEl.ID = 0
        for record in dataset:
            payEl.ID += 1
            payEl.code = str(record['ID'])
            payEl.name = str(record['NM'])
            payEl.description = payEl.name + '(' + payEl.code + ')'
            payEl.write_record(f)
            dictionary.set_PayElID(payEl.code, payEl.ID)
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]


def append_hr_payEl(ID, code, name, src_path, dst_path):
    dst_file = dst_path + 'hr_payEl.csv'
    try:
        f = open(dst_file, 'a+')
        payEl = PayEl()
        payEl.ID = ID
        payEl.code = code
        payEl.name = name
        payEl.description = payEl.name + '(' + payEl.code + ')'
        payEl.write_record(f)
        return ID
    except:
        print 'Error append ', dst_file, sys.exc_info()[1]
        return 0
