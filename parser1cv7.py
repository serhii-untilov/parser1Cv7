#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
from dbfpy import dbf

src_path = 'C:\\Users\\serhii.untilov\\tmp\\1С\\'
dst_path = src_path

def hr_position():
    dataset = dbf.Dbf(src_path + 'DOL.DBF')
    f = open(dst_path + 'Довідник посад (не штатних позицій) (hr_position).csv', 'w+')
    f.write('ID;code;name\r\n')
    for record in dataset:
        cd = record['CD']
        nm = record['NM']
        f.write('%s;%s;%s\r\n' % (cd, cd, nm))
    dataset.close()


def hr_workSchedule():
    dataset = dbf.Dbf(src_path + 'GRF.DBF')
    f = open(dst_path + 'Графіки роботи (hr_workSchedule).csv', 'w+')
    f.write('ID;code;name\r\n')
    id = 0
    for record in dataset:
        id += 1
        cd = record['CD']
        nm = record['NM']
        f.write('%d;%s;%s\r\n' % (id, cd, nm))
    dataset.close()


def hr_dictStaffCat():
    dataset = dbf.Dbf(src_path + 'KAT.DBF')
    f = open(dst_path + 'Категорії персоналу (hr_dictStaffCat).csv', 'w+')
    f.write('ID;code;name\r\n')
    id = 0
    for record in dataset:
        id += 1
        cd = record['CD']
        nm = record['NM']
        f.write('%d;%s;%s\r\n' % (id, cd, nm))
    dataset.close()


def hr_employee():
    dataset = dbf.Dbf(src_path + 'LS.DBF')
    f = open(dst_path + 'Працівники (hr_employee).csv', 'w+')
    f.write('ID;lastName;firstName;middleName;shortFIO;fullFIO;genName;datName;accusativeName;insName;tabNum;state;sexType;birthDate;taxCode;phoneMobile;phoneWorking;phoneHome;email;description;locName;dayBirthDate;monthBirthDate;yearBirthDate\r\n')
    id = 0
    for record in dataset:
        id = record['ID']
        name = record['FIO'].split(' ')
        lastName = name[0]
        firstName = name[1]
        middleName = name[2]
        shortFIO = name[0] + ' ' + name[1][0] + '.' + name[2][0] + '.' 
        fullFIO = record['FIO']
        f.write('%d;%s;%s;%s;%s;%s\r\n' % (id, lastName, firstName, middleName, shortFIO, fullFIO))
    dataset.close()


if __name__ == '__main__':
    hr_position()
    hr_workSchedule()
    hr_dictStaffCat()
    hr_employee()
