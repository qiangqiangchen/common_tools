# -*- coding:utf-8 -*-
import os

import xlrd


#对于有合并单元格的用例进行读取
def get_all_case(data_file,sheet):
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    model_count=len(sh.merged_cells)    #模块总数
    case_header=sh.row_values(0,start_colx=2)
    for merged in sh.merged_cells:
        case_info={}
        case_info['model']=sh.cell_value(merged[0],merged[2])   #用例模块号
        case_info['cases']=[]
        for row in range(merged[0],merged[1]):
            # 获取用例信息和标题组装成字典
            case=dict()
            case.update({'No':sh.cell_value(row, 0)})
            case.update(zip(case_header, sh.row_values(row,start_colx=2)))
            case_info['cases'].append(case)
        yield case_info

def is_merged(sh,row):
    for merged in sh.merged_cells:
        if row in range(merged[0],merged[1]):
            return merged
    return False

#对于有合并单元格的用例进行读取
def get_all_case2(data_file,sheet):
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    model_count=len(sh.merged_cells)    #模块总数
    case_header=sh.row_values(0,start_colx=2)
    index=1
    while index<sh.nrows:
        case_info = {}
        merged_data=is_merged(sh,index)
        if merged_data:
            case_info['model'] = sh.cell_value(merged_data[0], 1)  # 用例模块号
            case_info['cases'] = []
            for i in range(merged_data[0],merged_data[1]):
                # 获取用例信息和标题组装成字典
                case=dict()
                case.update({'No':sh.cell_value(i, 0)})
                case.update(zip(case_header, sh.row_values(i,start_colx=2)))
                case_info['cases'].append(case)
            index=merged_data[1]
        else:
            case_info['model']= sh.cell_value(index,1)
            case_info['cases'] = []
            case = dict()
            case.update({'No': sh.cell_value(index, 0)})
            case.update(zip(case_header, sh.row_values(index, start_colx=2)))
            case_info['cases'].append(case)
            index+=1
        yield case_info

#以列表形式获取全部excel中的内容
def excel_to_list(data_file, sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    header = sh.row_values(0)  # 获取第一行标题
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始获取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list

#在所有的列表中获取指定内容
def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data
    return None


def get_row(data_file,sheet,row):
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    header = sh.row_values(0)  # 获取第一行标题
    return dict(zip(header, sh.row_values(row)))


if __name__ == '__main__':
    data_path=r'../data/附件2：incopat导出字段-默认规则.xlsx'
    data=excel_to_list(data_path,'Sheet2')
    print(data)




