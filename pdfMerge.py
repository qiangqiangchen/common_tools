# -*- coding:utf-8 -*-
import os

import img2pdf
from PyPDF2 import PdfFileReader, PdfFileWriter

"""
合并PDF
"""



#获取给定目录下所有PDF文件，返回一个文件列表
def getFileName(filepath,filter='pdf'):
    file_list = []
    filter_list=[]
    if isinstance(filter,str):
        filter_list.append(filter)
    else:
        filter_list=filter
    filter_list=list(map(lambda x:x.lower(),filter_list))
    for root, dirs, files in os.walk(filepath):
        for filepath in files:
            #if filepath.lower().endswith(filter):
            if filepath.lower().split('.')[-1] in filter_list:
                file_list.append(os.path.join(root, filepath))
    return file_list

#将所有PDF文件写入一个文件
def pdfMerge(filepath, outfile):
    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)
    for i in pdf_fileName:
        print("正在合并:{}".format(i))
        input = PdfFileReader(open(i, 'rb'))
        pageCount = input.getNumPages()
        print(pageCount)
        for page in range(pageCount):
            output.addPage(input.getPage(page))
            print("------>正在写入第{}页".format(page))
    output.write(open(outfile, 'wb'))

def img_to_pdf(filepath, outfile):
    img_list=getFileName(filepath,filter=['jpg','jpeg','png'])
    a4input=(img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
    layout_fun=img2pdf.get_layout_fun(a4input)
    with open(outfile,'wb') as f:
        f.write(img2pdf.convert(img_list,layout_fun=layout_fun))
    print("{}写入完成".format(outfile))

if __name__ == "__main__":
    img_dir=r'E:\pandownload\韩漫\中文合集8部\约炮APP 1-6\1'
    #pdf_dir = r"XXXXX"
    out_path = r"F:\piccc\pic.pdf"
    # pdfMerge(pdf_dir, out_path)
    # img_to_pdf(img_dir,out_path)

