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
        print(u"正在合并:{}".format(i))
        input = PdfFileReader(open(i, 'rb'))
        pageCount = input.getNumPages()
        print(pageCount)
        for page in range(pageCount):
            output.addPage(input.getPage(page))
            #print(u"------>正在写入第{}页".format(page))
    output.write(open(outfile, 'wb'))
    print(u"<------{}  写入完成".format(outfile))

def img_to_pdf(filepath, outfile):
    img_list=getFileName(filepath,filter=['jpg','jpeg','png'])
    a4input=(img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
    layout_fun=img2pdf.get_layout_fun(a4input)
    with open(outfile,'wb') as f:
        f.write(img2pdf.convert(img_list,layout_fun=layout_fun))
    print("u{}写入完成".format(outfile))

if __name__ == "__main__":
    base_dir=r'E:\Temp\分类\图片\【重金自购】【实力坑女友系列】被男友换图流出的姑娘们精品11'
    #pdf_dir = r"XXXXX"
    pdf_name=base_dir.split("\\")[-1]
    out_path=os.path.join(r"E:\Temp\分类\hanman",pdf_name+'.pdf')
    #pdfMerge(base_dir, out_path)
    img_to_pdf(base_dir,out_path)

