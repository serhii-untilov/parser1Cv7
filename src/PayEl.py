#!/usr/bin/env python2
import sys


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
