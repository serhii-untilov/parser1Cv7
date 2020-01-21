#!/usr/bin/env python2
import sys
from datetime import datetime
from dbfpy import dbf


def hr_employeeNumber(src_path, dst_path):
    dst_file = dst_path + 'hr_employeeNumber.csv'
    try:
        dataset = dbf.Dbf(src_path + 'LS.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;employeeID;taxCode;tabNum;dateFrom;dateTo;description;payOutID;personalAccount\n')
        for record in dataset:
            ID = str(record['TN']) # str(record['ID'])
            employeeID = str(record['ID'])
            taxCode = record['NLP']
            tabNum = str(record['TN'])
            dateFrom = record['BEG'] and record['BEG'] or ''
            dateTo = record['END'] and record['END'] or ''
            description = record['FIO'] + ' (' + str(record['TN']) + ')'
            payOutID = ''
            personalAccount = record['BANKRAH']
            f.write('%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % 
                (ID,employeeID,taxCode,tabNum,dateFrom,dateTo,description,payOutID,personalAccount))
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
