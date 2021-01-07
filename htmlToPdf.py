import sys, os
from datetime import date, timedelta
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QMarginsF
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPageLayout, QPageSize

def printPDF(url):
    app = QtWidgets.QApplication(sys.argv)
    loader = QtWebEngineWidgets.QWebEngineView()  #实例化一个WebEngineView
    loader.setZoomFactor(1)  #设置视图缩放比例
    loader.load(QtCore.QUrl(url))  #  求情html文件

    layout = QPageLayout(
        QPageSize(QPageSize.A4),   #设置打印纸张大小
        QPageLayout.Portrait, QMarginsF(0, 0, 0, 0)   #四边距
    )

    def printFinished():
        '''
        当PDF完成之后，调用此逻辑，打印相关信息并退出此APP实例
        '''
        page = loader.page()
        print("%s Printing Finished!" % page.title())
        app.exit()

    def printToPDF(finished):
        loader.show()
        page = loader.page()
        #调用printToPdf方法，下载PDF
        page.printToPdf("%s.pdf" % page.title(), layout)  

    #打印PDF结束后连接到关闭APP实例方法
    loader.page().pdfPrintingFinished.connect(printFinished)
    #加载完成后连接到PDF打印方法
    loader.loadFinished.connect(printToPDF)

    app.exec_()


if __name__ == '__main__':
    printPDF("https://shici.store/poetry-calendar/")
