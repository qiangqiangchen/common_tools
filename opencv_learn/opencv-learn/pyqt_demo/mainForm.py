# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCamera = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera.setGeometry(QtCore.QRect(60, 70, 150, 150))
        self.labelCamera.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCamera.setObjectName("labelCamera")
        self.labelCapture = QtWidgets.QLabel(self.centralwidget)
        self.labelCapture.setGeometry(QtCore.QRect(300, 70, 150, 150))
        self.labelCapture.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCapture.setObjectName("labelCapture")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(550, 70, 150, 150))
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        self.btnOpenCamera = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenCamera.setGeometry(QtCore.QRect(100, 390, 75, 23))
        self.btnOpenCamera.setObjectName("btnOpenCamera")
        self.btnCapture = QtWidgets.QPushButton(self.centralwidget)
        self.btnCapture.setGeometry(QtCore.QRect(240, 390, 75, 23))
        self.btnCapture.setObjectName("btnCapture")
        self.btnReadImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnReadImage.setGeometry(QtCore.QRect(380, 390, 75, 23))
        self.btnReadImage.setObjectName("btnReadImage")
        self.btnGray = QtWidgets.QPushButton(self.centralwidget)
        self.btnGray.setGeometry(QtCore.QRect(510, 390, 75, 23))
        self.btnGray.setObjectName("btnGray")
        self.btnThreshold = QtWidgets.QPushButton(self.centralwidget)
        self.btnThreshold.setGeometry(QtCore.QRect(640, 390, 75, 23))
        self.btnThreshold.setObjectName("btnThreshold")
        self.cbThresholdSelect = QtWidgets.QComboBox(self.centralwidget)
        self.cbThresholdSelect.setGeometry(QtCore.QRect(100, 450, 150, 22))
        self.cbThresholdSelect.setObjectName("cbThresholdSelect")
        self.btnThresholdOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnThresholdOk.setGeometry(QtCore.QRect(260, 450, 81, 23))
        self.btnThresholdOk.setObjectName("btnThresholdOk")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnOpenCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)
        self.btnCapture.clicked.connect(MainWindow.btnCapture_Clicked)
        self.btnReadImage.clicked.connect(MainWindow.btnReadImage_Clicked)
        self.btnGray.clicked.connect(MainWindow.btnGray_Clicked)
        self.btnThreshold.clicked.connect(MainWindow.btnThreshold_Clicked)
        self.cbThresholdSelect.currentIndexChanged['QString'].connect(MainWindow.cbThresholdSelect_currentIndexChanged)
        self.btnThresholdOk.clicked.connect(MainWindow.btnThresholdOk_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelCamera.setText(_translate("MainWindow", "摄像头"))
        self.labelCapture.setText(_translate("MainWindow", "捕获图"))
        self.labelResult.setText(_translate("MainWindow", "结果图"))
        self.btnOpenCamera.setText(_translate("MainWindow", "打开摄像头"))
        self.btnCapture.setText(_translate("MainWindow", "捕获图片"))
        self.btnReadImage.setText(_translate("MainWindow", "打开图片"))
        self.btnGray.setText(_translate("MainWindow", "灰度化"))
        self.btnThreshold.setText(_translate("MainWindow", "自适应阈值"))
        self.btnThresholdOk.setText(_translate("MainWindow", "固定阈值分割"))

