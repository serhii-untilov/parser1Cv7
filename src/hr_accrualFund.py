#!/usr/bin/env python2
# coding=cp1251
import sys
from datetime import datetime
from dbfpy import dbf
from Dictionary import Dictionary
from AccrualFund import AccrualFund


def hr_accrualFund(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_accrualFund.csv'
    try:
        f = open(dst_file, 'w+')
        accrualFund = AccrualFund()
        accrualFund.write_header(f)
        accrualFund.ID = 0

        _read_DBF(src_path + 'ESV.DBF', accrualFund, f, dictionary)

    except:
        print 'Error making ', dst_file, sys.exc_info()[1]


def _read_DBF(src_file, accrualFund, f, dictionary):
    dataset = dbf.Dbf(src_file)
    for record in dataset:
        if (dictionary.isSkipEmployee(record['TN'])):
            continue
        if (record['UP'] is not None and record['UP'] < dictionary.arcMinDate):
            continue
        code = record['CD']
        accrualFund.ID += 1
        accrualFund.periodCalc = record['UP']
        accrualFund.periodSalary = record['RP']
        accrualFund.tabNum = str(record['TN'])
        accrualFund.taxCode = dictionary.get_TaxCode(accrualFund.tabNum)
        accrualFund.employeeNumberID = accrualFund.tabNum = str(record['TN'])
        accrualFund.payFundID = dictionary.get_PayFundID(code)
        accrualFund.sourceSum = record['SOURCE'] != 0 and str(record['SOURCE']) or '0'
        baseSum = record['BASESUM'] + record['DOPLBASE']
        accrualFund.baseSum = baseSum != 0 and str(baseSum) or ''
        paySum = record['SUM'] + record['DOPL']
        accrualFund.paySum = paySum != 0 and str(paySum) or ''
        accrualFund.addMinSum = record['DOPLBASE'] != 0 and str(record['DOPLBASE']) or ''
        accrualFund.write_record(f)
    dataset.close()
