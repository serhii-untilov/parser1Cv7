#!/usr/bin/env python2
import sys
from dbfpy import dbf


def hr_dictStaffCat(src_path, dst_path):
    dst_file = dst_path + 'hr_dictStaffCat.csv'
    try:
        dataset = dbf.Dbf(src_path + 'KAT.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;code;name\r\n')
        id = 0
        for record in dataset:
            id += 1
            cd = record['CD']
            nm = record['NM']
            f.write('%d;%s;%s\r\n' % (id, cd, nm))
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
