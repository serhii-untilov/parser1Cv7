#!/usr/bin/env python2
import sys
from dbfpy import dbf


def hr_dictPosition(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_dictPosition.csv'
    try:
        dataset = dbf.Dbf(src_path + 'DOL.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;code;name\n')
        for record in dataset:
            ID = record['CD']
            code = str(record['CD'])
            name = record['NM']
            f.write('%d;%s;%s\n' % (ID, code, name))
            dictionary.set_DictPositionName(code, name)
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
