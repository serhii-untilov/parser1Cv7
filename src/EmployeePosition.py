#!/usr/bin/env python2
import sys


class EmployeePosition:
    def __init__(self):
        self.ID = 0
        self.employeeID = ''
        self.taxCode = ''
        self.tabNum = ''
        self.employeeNumberID = ''
        self.departmentID = ''
        self.positionID = ''
        self.dateFrom = ''
        self.dateTo = ''
        self.changeDateTo = ''
        self.workScheduleID = ''
        self.workerType = ''
        self.mtCount = ''
        self.description = ''
        self.dictRankID = ''
        self.dictStaffCatID = ''
        self.payElID = ''
        self.accrualSum = ''
        self.raiseSalary = ''
        self.isIndex = ''
        self.isActive = ''
        self.workPlace = ''
        self.dictFundSourceID = ''
        self.dictCategoryECBID = ''
        self.accountID = ''

    def clear(self):
        self.__init__()

    def write_header(self, f):
        f.write('ID;employeeID;taxCode;tabNum;employeeNumberID;departmentID;positionID;dateFrom;dateTo;changeDateTo;' + 
            'workScheduleID;workerType;mtCount;description;dictRankID;dictStaffCatID;payElID;accrualSum;raiseSalary;' + 
            'isIndex;isActive;workPlace;dictFundSourceID;dictCategoryECBID;accountID\n')

    def write_record(self, f):
        f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (
            self.ID,self.employeeID,self.taxCode,self.tabNum,self.employeeNumberID,self.departmentID,self.positionID,
            self.dateFrom,self.dateTo,self.changeDateTo,self.workScheduleID,self.workerType,self.mtCount,self.description,
            self.dictRankID,self.dictStaffCatID,self.payElID,self.accrualSum,self.raiseSalary,self.isIndex,self.isActive,
            self.workPlace,self.dictFundSourceID,self.dictCategoryECBID,self.accountID))
