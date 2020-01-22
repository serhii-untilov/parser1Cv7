#!/usr/bin/env python2
import sys
from dbfpy import dbf
from Position import Position


def hr_position(src_path, dst_path, dictionary):
    dst_file = dst_path + 'hr_position.csv'
    try:
        f = open(dst_file, 'w+')
        position = Position()
        position.write_header(f)
        dataset = dbf.Dbf(src_path + 'PRK.DBF')
        position_list = set()
        for record in dataset:
            department_code = record['PDR']
            if (department_code):
                department_id = dictionary.get_DepartmentID(department_code)
                dictPosition_id = record['DOL']
                if (department_id and dictPosition_id):
                    position.ID = int(department_id) * 10000 + dictPosition_id
                    if (position.ID in position_list):
                        continue
                    position_list.add(position.ID)
                    position.code = str(dictPosition_id)
                    position.name = dictionary.get_DictPositionName(position.code)
                    position.psCategory = ''
                    position.positionType = ''
                    position.description = ''
                    position.write_record(f)
        dataset.close()
    except:
        print 'Error making ', dst_file, sys.exc_info()[1]
