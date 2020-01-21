#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
from dbfpy import dbf
from Dictionary import Dictionary


def hr_payEl(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_payEl.csv'
    try:
        dataset = dbf.Dbf(src_path + 'VO.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;code;name;methodID;description;dateFrom;dateTo;roundUpTo;isAutoCalc;isRecalculate;calcProportion;' + 
            'calcSumType;periodType;dictExperienceID;calcMounth;averageMethod;typePrepayment;prepaymentDay;dictFundSourceID\n')
        ID = 0
        for record in dataset:
            ID += 1
            code = str(record['ID'])
            name = str(record['NM'])
            methodID = str(record['FLG1'])
            description = name + '(' + code + ')'
            dateFrom = ''
            dateTo = ''
            roundUpTo = '2'
            isAutoCalc = '1'
            isRecalculate = '1'
            calcProportion = ''
            calcSumType = ''
            periodType = ''
            dictExperienceID = ''
            calcMounth = ''
            averageMethod = ''
            typePrepayment = ''
            prepaymentDay = ''
            dictFundSourceID = ''
            f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % 
                (ID, code, name, methodID, description, dateFrom, dateTo, roundUpTo, isAutoCalc, isRecalculate, 
                    calcProportion, calcSumType, periodType, dictExperienceID, calcMounth, averageMethod, typePrepayment, 
                        prepaymentDay, dictFundSourceID))
            dictionary.set_PayElID(code, ID)
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
