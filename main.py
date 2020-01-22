#!/usr/bin/env python2
import sys
import argparse
import os
import os.path
import re
from datetime import datetime
from dbfpy import dbf
from src.Dictionary import Dictionary
from src.hr_dictPosition import hr_dictPosition
from src.hr_position import hr_position
from src.hr_workSchedule import hr_workSchedule
from src.hr_dictStaffCat import hr_dictStaffCat
from src.hr_employee import hr_employee
from src.hr_payEl import hr_payEl
from src.hr_employeeNumber import hr_employeeNumber
from src.hr_employeePosition import hr_employeePosition
from src.hr_employeeAccrual import hr_employeeAccrual
from src.hr_accrual import hr_accrual
from src.hr_department import hr_department


DESCRIPTION = '1C v7 parser'
VERSION = '1.0 (20.01.2020)'
AUTHOR = 'USV'


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

    dictionary = Dictionary(namespace.src_path, namespace.dst_path)

    hr_dictPosition(namespace.src_path, namespace.dst_path, dictionary)
    hr_department(namespace.src_path, namespace.dst_path, dictionary)
    hr_workSchedule(namespace.src_path, namespace.dst_path)
    hr_dictStaffCat(namespace.src_path, namespace.dst_path)
    hr_payEl(namespace.src_path, namespace.dst_path, dictionary)
    hr_position(namespace.src_path, namespace.dst_path, dictionary)

    hr_employee(namespace.src_path, namespace.dst_path, dictionary)
    hr_employeeNumber(namespace.src_path, namespace.dst_path)
    hr_employeePosition(namespace.src_path, namespace.dst_path, dictionary)
    hr_employeeAccrual(namespace.src_path, namespace.dst_path, dictionary)
    hr_accrual(namespace.src_path, namespace.dst_path, dictionary)

