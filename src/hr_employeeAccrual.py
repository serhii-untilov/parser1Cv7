#!/usr/bin/env python2
import sys
from datetime import datetime
from dbfpy import dbf
from Dictionary import Dictionary


def hr_employeeAccrual(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_employeeAccrual.csv'
    try:
        dataset = dbf.Dbf(src_path + 'NCH.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;employeeID;tabNum;employeeNumberID;payElID;dateFrom;dateTo;accrualSum;accrualRate;orderNumber;' + 
            'orderDatefrom;taxCode\n')
        ID = 0
        for record in dataset:
            ID += 1
            employeeID = str(record['TN']) # str(record['ID'])
            tabNum = str(record['TN'])
            employeeNumberID = str(record['TN'])
            payElID = dictionary.get_PayElID(record['CD'])
            dateFrom = record['DATN'] and record['DATN'] or ''
            dateTo = record['DATK'] and record['DATK'] or '9999-12-31'
            accrualSum = str(record['SM'])
            accrualRate = str(record['PRC'])
            orderNumber = record['CDPR']
            orderDatefrom = ''
            taxCode = dictionary.get_TaxCode(tabNum)
            f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (ID, employeeID, tabNum, employeeNumberID, payElID, 
                dateFrom, dateTo, accrualSum, accrualRate, orderNumber, orderDatefrom, taxCode))
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
