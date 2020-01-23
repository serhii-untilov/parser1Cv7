#!/usr/bin/env python2
import sys
from dbfpy import dbf
from Dictionary import Dictionary
from PayEl import PayEl

def hr_payEl(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_payEl.csv'
    try:
        dataset = dbf.Dbf(src_path + 'VO.DBF')
        f = open(dst_file, 'w+')
        payEl = PayEl()
        payEl.write_header(f)
        payEl.ID = 0
        for record in dataset:
            payEl.ID += 1
            payEl.code = str(record['ID'])[:32]
            payEl.name = str(record['NM'])
            payEl.description = payEl.name + '(' + payEl.code + ')'
            payEl.write_record(f)
            dictionary.set_PayElID(payEl.code, payEl.ID)
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
