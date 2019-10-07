#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/7 13:44 
@Description:  面部识别
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from FaceIdentify import Ui_Form
from baiduface import BaiduFaceIdentify

class FaceIdentifyTool(QWidget):
    def __init__(self):
        super(FaceIdentifyTool, self).__init__()
        self.bfi = BaiduFaceIdentify()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("./ttt.ico"))

        self.ui.pushButton_2.clicked.connect(self.loadImage)
        self.ui.pushButton.clicked.connect(self.identify)

    def loadImage(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, "打开文件", ".", "图像文件(*.jpg *.png)")
        self.ui.label.setPixmap(QPixmap(self.fname).scaled(400, 300, Qt.KeepAspectRatio))
        self.ui.lineEdit.setText(self.fname)

    def identify(self):
        result = self.bfi.parse_face_pic(self.fname)
        print(result)
        self.ui.label_2.setFont(QFont("Arial", 12))
        if result:
            str = ""
            for k, v  in result.items():
                str += (k + ":" + v + "\n")
            self.ui.label_2.setText(str)
        else:
            self.ui.label_2.setText("未识别到人脸")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FaceIdentifyTool()
    main.show()
    sys.exit(app.exec_())
