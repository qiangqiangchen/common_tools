# -*- coding:utf-8 -*-
import os

from PyPDF2 import PdfFileReader, PdfFileWriter

"""
合并PDF
"""



#获取给定目录下所有PDF文件，返回一个文件列表
def getFileName(filepath):
    file_list = []
    for root, dirs, files in os.walk(filepath):
        for filepath in files:
            if filepath.lower().endswith("pdf"):
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


if __name__ == "__main__":
    pdf_dir = r"XXXXX"
    out_path = r"XXXX.pdf"
    pdfMerge(pdf_dir, out_path)
