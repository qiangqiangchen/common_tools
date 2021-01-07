# -*- coding: utf-8 -*-

import sys
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from mainForm import Ui_MainWindow


class PyQtMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Threshold_index=None
        Threshold=["THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV"]
        self.cbThresholdSelect.addItems(Threshold)

        self.camera = cv2.VideoCapture(0)
        self.is_camera_opened = False  # 摄像头有没有打开标记

        # 定时器：30ms捕获一帧
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(30)



    def getQImg(self, img, img_type):
        """
         # Qt显示图片时，需要先转换成QImgage类型
        :param img:
        :param img_type:
        :return: QImgage类型图片
        """
        if len(img.shape) == 2:
            rows, cols, = img.shape
            bytesPerLine = cols
        else:
            rows, cols, channels = img.shape
            bytesPerLine = channels * cols

        QImg = QImage(img.data, cols, rows, bytesPerLine, img_type)
        return QImg

    def btnOpenCamera_Clicked(self):
        """
        打开和关闭摄像头
        :return:
        """
        self.is_camera_opened = ~self.is_camera_opened

        if self.is_camera_opened:
            self.btnOpenCamera.setText("关闭摄像头")
            self._timer.start()
        else:
            self.btnOpenCamera.setText("打开摄像头")
            self._timer.stop()

    def btnCapture_Clicked(self):
        """
        捕获图片
        :return:
        """
        if not self.is_camera_opened:
            return
        self.captured = self.frame

        rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)

        self.labelCapture.setPixmap(
            QPixmap.fromImage(QImg).scaled(self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def btnReadImage_Clicked(self):
        """
        从本地读取图片
        :return:
        """
        filename, _ = QFileDialog.getOpenFileName(self, "打开图片")
        if filename:
            self.captured = cv2.imread(str(filename))

            self.captured = cv2.cvtColor(self.captured, cv2.COLOR_BGR2RGB)

            QImg = self.getQImg(self.captured, QImage.Format_RGB888)
            self.labelCapture.setPixmap(
                QPixmap.fromImage(QImg).scaled(self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )

    def btnGray_Clicked(self):
        """
        灰度化
        :return:
        """
        if not hasattr(self, "captured"):
            return

        gyay_captured = cv2.cvtColor(self.captured, cv2.COLOR_RGB2GRAY)
        QImg = self.getQImg(gyay_captured, QImage.Format_Indexed8)
        self.labelResult.setPixmap(
            QPixmap.fromImage(QImg).scaled(self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

    def btnThreshold_Clicked(self):
        """
        阈值分割
        :return:
        """
        if not hasattr(self, "captured"):
            return
        threshold_captured = cv2.cvtColor(self.captured,cv2.COLOR_BGR2GRAY)
        threshold_captured = cv2.adaptiveThreshold(threshold_captured, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
        QImg = self.getQImg(threshold_captured, QImage.Format_Indexed8)
        self.labelResult.setPixmap(
            QPixmap.fromImage(QImg).scaled(self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

    @QtCore.pyqtSlot()
    def _queryFrame(self):
        """
        循环捕获图片
        :return:
        """
        ret, self.frame = self.camera.read()
        self.new_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        QImg = self.getQImg(self.new_frame, QImage.Format_RGB888)
        self.labelCamera.setPixmap(
            QPixmap.fromImage(QImg).scaled(self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )


    def cbThresholdSelect_currentIndexChanged(self,text):
        if text:
            self.Threshold_index=text

    def btnThresholdOk_Clicked(self):
        if not hasattr(self, "captured"):
            return
        img=cv2.cvtColor(self.captured,cv2.COLOR_BGR2GRAY)
        if self.Threshold_index == "THRESH_BINARY":
            ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        elif self.Threshold_index == "THRESH_BINARY_INV":
            ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        elif self.Threshold_index == "THRESH_TRUNC":
            ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
        elif self.Threshold_index == "THRESH_TOZERO":
            ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
        elif self.Threshold_index == "THRESH_TOZERO_INV":
            ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
        QImg = self.getQImg(th1, QImage.Format_Indexed8)
        self.labelResult.setPixmap(
            QPixmap.fromImage(QImg).scaled(self.labelCapture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = PyQtMainEntry()
    windows.show()
    sys.exit(app.exec_())
