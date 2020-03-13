#!/usr/bin/env python2
import sys
from datetime import datetime
from dbfpy import dbf


def renewalTN(src_path, dst_path, dictionary):
    dst_file = dst_path + 'renewalTN.csv'
    try:
        dataset = dbf.Dbf(src_path + 'LS.DBF')
        f = open(dst_file, 'w+')
        f.write('taxCode;tabNum\n')
        for record in dataset:
            if (dictionary.isSkipEmployee(record['TN'])):
                continue
            taxCode = record['NLP']
            tabNum = str(record['TN'])
            f.write('%s;%s\n' % 
                (taxCode,tabNum))
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
