#!/usr/bin/env python2
# coding=cp1251
import sys
from datetime import datetime
from dbfpy import dbf
from Dictionary import Dictionary


def setPayElUsed(src_path, dictionary):
    try:
        _read_DBF(src_path + 'RL.DBF', dictionary, '')
        _read_DBF(src_path + 'RL_Dogl.DBF', dictionary, '')
        _read_DBF(src_path + 'RL_Lik_P.DBF', dictionary, '')
        _read_DBF(src_path + 'RL_Lik_F.DBF', dictionary, '_ФСС')
    except:
        print 'Error making PayElCode', sys.exc_info()[1]


def _read_DBF(src_file, dictionary, suffix):
    dataset = dbf.Dbf(src_file)
    for record in dataset:
        if (record['CD'] == 'НачальноеСальдо'):
            continue
        if (dictionary.isSkipEmployee(record['TN'])):
            continue
        if (record['UP'] is not None and record['UP'] < dictionary.arcMinDate):
            continue
        code = str(record['CD'])[:32] + suffix
        dictionary.setPayElCode(code)
    dataset.close()
