#!/usr/bin/env python2
import sys
from datetime import datetime
from dbfpy import dbf
from Dictionary import Dictionary


def hr_employee(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_employee.csv'
    try:
        dataset = dbf.Dbf(src_path + 'LS.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;lastName;firstName;middleName;shortFIO;fullFIO;genName;datName;tabNum;sexType;birthDate;taxCode;email;description;locName;dayBirthDate;monthBirthDate;yearBirthDate\n')
        for record in dataset:
            if (record['END'] is not None and record['END'] < dictionary.arcMinDate and dictionary.getAccrualSize(record['TN']) == 0):
                print('TabNum {} is skipped. Dismissal date is {}'.format(record['TN'], record['END']))
                dictionary.setSkipEmployee(record['TN'])
                continue
            ID = str(record['TN']) # str(record['ID'])
            name = record['FIO'].split(' ')
            lastName = name[0]
            firstName = name[1]
            middleName = name[2]
            shortFIO = name[0] + ' ' + name[1][0] + '.' + name[2][0] + '.' 
            fullFIO = record['FIO']
            genName = record['FIOR']
            datName = record['FIOD']
            tabNum = str(record['TN'])
            sexType = record['SEX'] == 1 and 'M' or record['SEX'] == 2 and 'W' or ''
            birthDate = str(record['DTROJ'] and record['DTROJ'] or '' )
            taxCode = record['NLP']
            email = record['EMAIL']
            description = record['FIO'] + ' (' + str(record['TN']) + ')'
            locName = record['FIO']
            dayBirthDate = record['DTROJ'] and record['DTROJ'].day or ''
            monthBirthDate = record['DTROJ'] and record['DTROJ'].month or ''
            yearBirthDate = record['DTROJ'] and record['DTROJ'].year or ''
            f.write('%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (ID, lastName, firstName, middleName, shortFIO, fullFIO, 
                genName, datName, tabNum, sexType, birthDate, taxCode, email, description, locName, dayBirthDate, monthBirthDate, yearBirthDate))
            dictionary.set_TaxCode(tabNum, taxCode)
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
