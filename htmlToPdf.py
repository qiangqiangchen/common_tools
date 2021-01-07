import sys, os
from datetime import date, timedelta
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QMarginsF
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPageLayout, QPageSize

def printPDF(url):
    app = QtWidgets.QApplication(sys.argv)
    loader = QtWebEngineWidgets.QWebEngineView()  #ʵ����һ��WebEngineView
    loader.setZoomFactor(1)  #������ͼ���ű���
    loader.load(QtCore.QUrl(url))  #  ����html�ļ�

    layout = QPageLayout(
        QPageSize(QPageSize.A4),   #���ô�ӡֽ�Ŵ�С
        QPageLayout.Portrait, QMarginsF(0, 0, 0, 0)   #�ı߾�
    )

    def printFinished():
        '''
        ��PDF���֮�󣬵��ô��߼�����ӡ�����Ϣ���˳���APPʵ��
        '''
        page = loader.page()
        print("%s Printing Finished!" % page.title())
        app.exit()

    def printToPDF(finished):
        loader.show()
        page = loader.page()
        #����printToPdf����������PDF
        page.printToPdf("%s.pdf" % page.title(), layout)  

    #��ӡPDF���������ӵ��ر�APPʵ������
    loader.page().pdfPrintingFinished.connect(printFinished)
    #������ɺ����ӵ�PDF��ӡ����
    loader.loadFinished.connect(printToPDF)

    app.exec_()


if __name__ == '__main__':
    printPDF("https://shici.store/poetry-calendar/")
