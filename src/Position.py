#!/usr/bin/env python2
import sys


class Position:
    def __init__(self):
        self.ID = 0
        self.code = ''
        self.name = ''
        self.fullName = ''
        self.parentUnitID = ''
        self.state = 'ACTIVE'
        self.psCategory = ''
        self.positionType = ''
        self.dictProfessionID = ''
        self.dictWagePayID = ''
        self.description = ''
        self.nameGen = ''
        self.nameDat = ''
        self.fullNameGen = ''	
        self.fullNameDat = ''
        self.nameOr = ''
        self.fullNameOr = ''	
        self.quantity = '0'
        self.personalType = ''
        self.positionCategory = ''	
        self.dictStatePayID = ''
        self.accrualSum = ''
        self.payElID = ''
        self.dictStaffCatID = ''
        self.dictFundSourceID = ''
        self.nameAcc = ''
        self.fullNameAcc = ''	
        self.entryOrderID = ''
        self.nameLoc = ''
        self.fullNameLoc = ''	
        self.nameNom = ''
        self.nameVoc = ''
        self.fullNameNom = ''	
        self.fullNameVoc = ''
        self.liquidate = '0'

    def write_header(self, f):
        f.write('ID;code;name;fullName;parentUnitID;state;psCategory;positionType;dictProfessionID;dictWagePayID;' +
            'description;nameGen;nameDat;fullNameGen;fullNameDat;nameOr;fullNameOr;quantity;personalType;' + 
            'positionCategory;dictStatePayID;accrualSum;payElID;dictStaffCatID;dictFundSourceID;nameAcc;' + 
            'fullNameAcc;entryOrderID;nameLoc;fullNameLoc;nameNom;nameVoc;fullNameNom;fullNameVoc;liquidate\n')

    def write_record(self, f):
        f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (
            self.ID,self.code,self.name,self.fullName,self.parentUnitID,self.state,self.psCategory,self.positionType
            ,self.dictProfessionID,self.dictWagePayID,self.description,self.nameGen,self.nameDat,self.fullNameGen
            ,self.fullNameDat,self.nameOr,self.fullNameOr,self.quantity,self.personalType,self.positionCategory
            ,self.dictStatePayID,self.accrualSum,self.payElID,self.dictStaffCatID,self.dictFundSourceID
            ,self.nameAcc,self.fullNameAcc,self.entryOrderID,self.nameLoc,self.fullNameLoc,self.nameNom,self.nameVoc
            ,self.fullNameNom,self.fullNameVoc,self.liquidate))
