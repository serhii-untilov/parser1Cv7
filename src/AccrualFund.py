#!/usr/bin/env python2
import sys


class AccrualFund:
    def __init__(self):
        self.ID = 0
        self.periodCalc = ''
        self.periodSalary = ''
        self.tabNum = ''
        self.taxCode = ''
        self.employeeNumberID = ''
        self.payFundID = ''
        self.sourceSum = ''
        self.baseSum = ''
        self.rate = ''
        self.paySum = ''
        self.addMinSum = ''

    def write_header(self, f):
        f.write('ID;periodCalc;periodSalary;tabNum;taxCode;employeeNumberID;payFundID;sourceSum;baseSum;rate;paySum;addMinSum\n')

    def write_record(self, f):
        f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (
            self.ID, self.periodCalc, self.periodSalary, self.tabNum, self.taxCode, self.employeeNumberID, 
            self.payFundID, self.sourceSum, self.baseSum, self.rate, self.paySum, self.addMinSum))
