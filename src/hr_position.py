#!/usr/bin/env python2
import sys
from dbfpy import dbf


def hr_position(src_path, dst_path):
    dst_file = dst_path + 'hr_position.csv'
    try:
        dataset = dbf.Dbf(src_path + 'DOL.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;code;name\r\n')
        for record in dataset:
            cd = record['CD']
            nm = record['NM']
            f.write('%s;%s;%s\r\n' % (cd, cd, nm))
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
