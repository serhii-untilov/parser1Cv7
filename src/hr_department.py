#!/usr/bin/env python2
import sys
from dbfpy import dbf


def hr_department(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_department.csv'
    try:
        dataset = dbf.Dbf(src_path + 'PDR.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;code;name;parentUnitID;state;fullName;description;nameGen;fullNameGen;nameDat;nameOr;' + 
            'fullNameGen;fullNameDat;dateFrom;dateTo\n')
        ID = 0
        for record in dataset:
            ID += 1
            code = record['ID']
            name = record['NM']
            parentUnitID = record['ID_PARENT'] and dictionary.get_DepartmentID(record['ID_PARENT']) or ''
            state = 'ACTIVE'
            fullName = record['NMF']
            description = name + ' (' + code + ')'
            nameGen = ''
            fullNameGen = ''
            nameDat =''
            nameOr = ''
            fullNameGen = ''
            fullNameDat = ''
            dateFrom = record['BEG']
            dateTo = record['END'] and record['END'] or ''
            f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (
                ID, code, name, parentUnitID, state, fullName, description, nameGen, fullNameGen, nameDat, nameOr,
                fullNameGen, fullNameDat, dateFrom, dateTo))
            dictionary.set_DepartmentID(code, ID)
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
