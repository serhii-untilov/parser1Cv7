#!/usr/bin/env python2
import sys
from datetime import datetime
from dbfpy import dbf
from Dictionary import Dictionary


def setAccrualSize(src_path, dst_path, dictionary):
    try:
        _read_DBF(src_path + 'RL.DBF', dictionary)
        _read_DBF(src_path + 'RL_Dogl.DBF', dictionary)
        _read_DBF(src_path + 'RL_Lik_F.DBF', dictionary)
        _read_DBF(src_path + 'RL_Lik_P.DBF', dictionary)

    except:
        print 'Accrual size calculating error. ', sys.exc_info()[1]


def _read_DBF(src_file, dictionary):
    dataset = dbf.Dbf(src_file)
    for record in dataset:
        if (record['UP'] is None or record['UP'] < dictionary.arcMinDate):
            continue
        dictionary.addAccrualSize(record['TN'])
    dataset.close()
