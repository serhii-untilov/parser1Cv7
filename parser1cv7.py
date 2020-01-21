#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import argparse
import os
import os.path
import re
from datetime import datetime
from dbfpy import dbf


DESCRIPTION = '1C v7 parser'
VERSION = '1.0 (20.01.2020)'
AUTHOR = 'USV'


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


def hr_workSchedule(src_path, dst_path):
    dst_file = dst_path + 'hr_workSchedule.csv'
    try:
        dataset = dbf.Dbf(src_path + 'GRF.DBF')
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


def hr_employee(src_path, dst_path):
    dst_file = dst_path + 'hr_employee.csv'
    try:
        dataset = dbf.Dbf(src_path + 'LS.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;lastName;firstName;middleName;shortFIO;fullFIO;genName;datName;tabNum;sexType;birthDate;taxCode;email;description;dayBirthDate;monthBirthDate;yearBirthDate\r\n')
        id = 0
        for record in dataset:
            id = str(record['ID'])
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
            birthDate = str(record['DTROJ'])
            taxCode = record['NLP']
            email = record['EMAIL']
            description = record['FIO'] + ' (' + str(record['TN']) + ')'
            locName = record['FIO']
            dayBirthDate = record['DTROJ'] and record['DTROJ'].day or ''
            monthBirthDate = record['DTROJ'] and record['DTROJ'].month or ''
            yearBirthDate = record['DTROJ'] and record['DTROJ'].year or ''
            f.write('%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\r\n' % (id, lastName, firstName, middleName, shortFIO, fullFIO, 
                genName, datName, tabNum, sexType, birthDate, taxCode, email, description, locName, dayBirthDate, monthBirthDate, yearBirthDate))
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]


def create_arg_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=AUTHOR, add_help=False)
    parser.add_argument('--src_path', '-s', action='store', help='Set path to a source files directory.')
    parser.add_argument('--dst_path', '-d', action='store', help='Set path to a destination files directory.')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s {}'.format(VERSION), help='Get programm\'s version.')
    parser.add_argument('--help', '-h', action='help', help='Help.')
    return parser


def set_default(namespace):
    if namespace.src_path is None:
        namespace.src_path = os.path.dirname(os.path.realpath(__file__))
    if namespace.dst_path is None:
        namespace.dst_path = namespace.src_path
    if namespace.src_path[-1] != '\\':
        namespace.src_path += '\\'
    if namespace.dst_path[-1] != '\\':
        namespace.dst_path += '\\'


if __name__ == '__main__':
    parser = create_arg_parser()
    namespace = parser.parse_args()
    set_default(namespace)
    print parser.description
    print namespace

    hr_position(namespace.src_path, namespace.dst_path)
    hr_workSchedule(namespace.src_path, namespace.dst_path)
    hr_dictStaffCat(namespace.src_path, namespace.dst_path)
    hr_employee(namespace.src_path, namespace.dst_path)
