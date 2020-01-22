#!/usr/bin/env python2
import sys
from dbfpy import dbf


def hr_dictPosition(src_path, dst_path):
    dst_file = dst_path + 'hr_dictPosition.csv'
    try:
        dataset = dbf.Dbf(src_path + 'DOL.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;code;name\n')
        for record in dataset:
            ID = record['CD']
            CD = str(record['CD'])
            NM = record['NM']
            f.write('%d;%s;%s\n' % (ID, CD, NM))
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
