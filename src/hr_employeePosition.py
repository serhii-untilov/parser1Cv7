#!/usr/bin/env python2
import sys
from datetime import datetime
import re
from dbfpy import dbf
import Dictionary
from EmployeePosition import EmployeePosition


def hr_employeePosition(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_employeePosition.csv'
    try:
        dataset = dbf.Dbf(src_path + 'PRK.DBF')
        f = open(dst_file, 'w+')
        employeePosition = EmployeePosition()
        employeePosition.write_header(f)
        employeePosition.clear()
        last_tabNum = 0
        ID = 0
        for record in dataset:
            ID += 1
            tabNum = str(record['TN'])
            if (last_tabNum != tabNum):
                employeePosition.clear()
            employeePosition.tabNum = tabNum
            employeePosition.ID = ID
            employeePosition.employeeID = record['TN']
            employeePosition.taxCode = dictionary.get_TaxCode(tabNum)
            employeePosition.employeeNumberID = record['TN']
            
            # positionID = record['DOL'] > 0 and str(record['DOL']) or ''
            if (record['PDR']):
                department_id = dictionary.get_DepartmentID(record['PDR'])
                employeePosition.departmentID = str(department_id)
                dictPosition_id = record['DOL']
                if (department_id and dictPosition_id):
                    employeePosition.positionID = int(department_id) * 10000 + dictPosition_id

            employeePosition.dateFrom = record['BEG'] and record['BEG'] or ''
            employeePosition.dateTo = ''
            if (record['STV']):
                employeePosition.mtCount = str(record['STV'])
            description = ''
            if (record['RAN']):
                employeePosition.dictRankID = record['RAN'] > 0 and str(record['RAN']) or ''
            if (record['KAD']):
                employeePosition.dictStaffCatID = re.sub('^0*', '', record['KAD'])
            employeePosition.payElID = ''
            if (record['OKL']):
                employeePosition.accrualSum = record['OKL']
            employeePosition.write_record(f)
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
