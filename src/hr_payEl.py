#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
from dbfpy import dbf


def hr_payEl(src_path, dst_path):
    dst_file = dst_path + 'hr_payEl.csv'
    try:
        dataset = dbf.Dbf(src_path + 'VO.DBF')
        f = open(dst_file, 'w+')
        f.write('ID;code;name;methodID;description;dateFrom;dateTo;roundUpTo;isAutoCalc;isRecalculate;calcProportion;calcSumType;periodType;dictExperienceID;calcMounth;averageMethod;typePrepayment;prepaymentDay;dictFundSourceID\n')
        id_csv = 0
        for record in dataset:
            id_csv += 1
            code_csv = str(record['ID'])
            name_csv = str(record['NM'])
            methodID_csv = str(record['FLG1'])
            description_csv = ''
            dateFrom_csv = ''
            dateTo_csv = ''
            roundUpTo_csv = ''
            isAutoCalc_csv = ''
            isRecalculate_csv = ''
            calcProportion_csv = ''
            calcSumType_csv = ''
            periodType_csv = ''
            dictExperienceID_csv = ''
            calcMounth_csv = ''
            averageMethod_csv = ''
            typePrepayment_csv = ''
            prepaymentDay_csv = ''
            dictFundSourceID_csv = ''
            f.write('%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (id_csv, code_csv, name_csv, methodID_csv, description_csv, dateFrom_csv, dateTo_csv, roundUpTo_csv, isAutoCalc_csv, isRecalculate_csv, calcProportion_csv, calcSumType_csv, periodType_csv, dictExperienceID_csv, calcMounth_csv, averageMethod_csv, typePrepayment_csv, prepaymentDay_csv, dictFundSourceID_csv))
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
