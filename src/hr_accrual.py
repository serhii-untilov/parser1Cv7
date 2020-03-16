#!/usr/bin/env python2
# coding=cp1251
import sys
from datetime import datetime
from dbfpy import dbf
from Dictionary import Dictionary
from Accrual import Accrual


def hr_accrual(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_accrual.csv'
    try:
        f = open(dst_file, 'w+')
        accrual = Accrual()
        accrual.write_header(f)
        accrual.ID = 0

        _read_DBF(src_path + 'RL.DBF', accrual, f, dictionary, '')
        _read_DBF(src_path + 'RL_Dogl.DBF', accrual, f, dictionary, '')
        _read_DBF(src_path + 'RL_Lik_P.DBF', accrual, f, dictionary, '')
        _read_DBF(src_path + 'RL_Lik_F.DBF', accrual, f, dictionary, '_ФСС')

    except:
        print 'Error making ', dst_file, sys.exc_info()[1]


def _read_DBF(src_file, accrual, f, dictionary, suffix):
    dataset = dbf.Dbf(src_file)
    for record in dataset:
        if (record['CD'] == 'НачальноеСальдо'):
            continue
        if (dictionary.isSkipEmployee(record['TN'])):
            continue
        if (record['UP'] is not None and record['UP'] < dictionary.arcMinDate):
            continue
        code = record['CD'] + suffix
        accrual.ID += 1
        accrual.periodCalc = record['UP']
        accrual.periodSalary = record['RP']
        accrual.tabNum = str(record['TN'])
        accrual.taxCode = dictionary.get_TaxCode(accrual.tabNum)
        accrual.employeeNumberID = accrual.tabNum = str(record['TN'])
        accrual.payElID	= dictionary.get_PayElID(code)
        accrual.paySum = record['SM'] != 0 and str(record['SM']) or ''
        accrual.days = record['DAYS'] != 0 and str(record['DAYS']) or ''
        accrual.hours = record['HRS'] != 0 and str(record['HRS']) or ''
        accrual.calculateDate = ''	
        accrual.flagsRec = str(8 | (record['STOR'] > 0 and 512 or 0)) # 8 - import, 512 - storno
        accrual.dateFrom = record['PR_BEG']
        accrual.dateTo = record['PR_END']
        accrual.write_record(f)
    dataset.close()
