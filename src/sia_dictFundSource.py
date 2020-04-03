#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
from Dictionary import Dictionary
from DictFundSource import DictFundSource


def sia_dictFundSource(src_path, dst_path, dictionary):
    dst_file = dst_path + 'sia_dictFundSource.csv'
    try:
        f = open(dst_file, 'w+')
        entity = DictFundSource()
        entity.write_header(f)
        entity.ID = 1
        entity.code = '1'
        entity.name = 'Джерело фінансування для заборгованості по зарплаті (змініть код і назву)'
        entity.write_record(f)
        dictionary.setDictFundSourceID(entity.code, entity.ID)
    except:
        print 'Error making ', dst_file, sys.exc_info()

