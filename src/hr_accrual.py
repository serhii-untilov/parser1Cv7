#!/usr/bin/env python2
import sys
from datetime import datetime
from dbfpy import dbf
from Dictionary import Dictionary


def hr_accrual(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_accrual.csv'
    try:
        dataset = dbf.Dbf(src_path + 'RL.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;periodCalc;periodSalary;tabNum;taxCode;employeeNumberID;payElID;baseSum;rate;paySum;days;hours;' + 
            'calculateDate;mask;flagsRec;flagsFix;planHours;planDays;maskAdd;dateFrom;dateTo;source;sourceID;' + 
                'dateFromAvg;dateToAvg;sumAvg\n')
        ID = 0
        for record in dataset:
            ID += 1
            periodCalc = record['UP']
            periodSalary = record['RP']
            tabNum = str(record['TN'])
            taxCode = dictionary.get_TaxCode(tabNum)
            employeeNumberID = tabNum = str(record['TN'])
            payElID	= dictionary.get_PayElID(record['CD'])
            baseSum = ''
            rate = ''
            paySum = record['SM'] != 0 and str(record['SM']) or ''
            days = record['DAYS'] != 0 and str(record['DAYS']) or ''
            hours = record['HRS'] != 0 and str(record['HRS']) or ''
            calculateDate = ''	
            mask = ''
            flagsRec = str(8 | (record['STOR'] > 0 and 512 or 0)) # 8 - import, 512 - storno
            flagsFix = ''	
            planHours = ''
            planDays = ''
            maskAdd	= ''
            dateFrom = record['PR_BEG']
            dateTo = record['PR_END']
            source = ''
            sourceID = ''
            dateFromAvg	= ''
            dateToAvg = ''
            sumAvg = ''
            f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % 
                (ID, periodCalc, periodSalary, tabNum, taxCode, employeeNumberID, payElID, baseSum, rate, paySum, days, hours, 
                    calculateDate, mask, flagsRec, flagsFix, planHours, planDays, maskAdd, dateFrom, dateTo, source, 
                        sourceID, dateFromAvg, dateToAvg, sumAvg))
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
