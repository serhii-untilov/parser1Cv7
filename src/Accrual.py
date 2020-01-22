#!/usr/bin/env python2
import sys


class Accrual:
    def __init__(self):
        self.ID = 0
        self.periodCalc = ''
        self.periodSalary = ''
        self.tabNum = ''
        self.taxCode = ''
        self.employeeNumberID = ''
        self.payElID = ''
        self.baseSum = ''
        self.rate = ''
        self.paySum = ''
        self.days = ''
        self.hours = ''
        self.calculateDate = ''	
        self.mask = ''
        self.flagsRec = ''
        self.flagsFix = ''	
        self.planHours = ''
        self.planDays = ''
        self.maskAdd	= ''
        self.dateFrom = ''
        self.dateTo = ''
        self.source = ''
        self.sourceID = ''
        self.dateFromAvg = ''
        self.dateToAvg = ''
        self.sumAvg = ''

    def write_header(self, f):
        f.write('ID;periodCalc;periodSalary;tabNum;taxCode;employeeNumberID;payElID;baseSum;rate;paySum;days;hours;' + 
            'calculateDate;mask;flagsRec;flagsFix;planHours;planDays;maskAdd;dateFrom;dateTo;source;sourceID;' + 
            'dateFromAvg;dateToAvg;sumAvg\n')

    def write_record(self, f):
        f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (
            self.ID, self.periodCalc, self.periodSalary, self.tabNum, self.taxCode, self.employeeNumberID, 
            self.payElID, self.baseSum, self.rate, self.paySum, self.days, self.hours, self.calculateDate, 
            self.mask, self.flagsRec, self.flagsFix, self.planHours, self.planDays, self.maskAdd, 
            self.dateFrom, self.dateTo, self.source, self.sourceID, self.dateFromAvg, self.dateToAvg, 
            self.sumAvg))
