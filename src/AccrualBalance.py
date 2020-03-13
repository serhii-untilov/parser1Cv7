#!/usr/bin/env python2
import sys


class AccrualBalance:
    def __init__(self):
        self.ID = 0
        self.employeeNumberID = 0
        self.periodCalc = ''
        self.dictFundSourceID = ''
        self.sumFrom = ''
        self.sumPlus = ''
        self.sumMinus = ''
        self.sumPay = ''
        self.sumTo = ''

    def write_header(self, f):
        f.write('ID;employeeNumberID;periodCalc;dictFundSourceID;sumFrom;sumPlus;sumMinus;sumPay;sumTo\n')

    def write_record(self, f):
        f.write('{};{};{};{};{};{};{};{};{}\n'.format(self.ID, self.employeeNumberID, self.periodCalc, self.dictFundSourceID,
            self.sumFrom, self.sumPlus, self.sumMinus, self.sumPay, self.sumTo))
