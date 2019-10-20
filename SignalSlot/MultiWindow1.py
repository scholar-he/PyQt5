#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/20 15:55 
@Description:  多窗口交互(1) : 不使用信号与槽

Win1

Win2

"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DateDialog import DateDialog


class MultiWindow1(QWidget):

    def __init__(self):
        super(MultiWindow1, self).__init__()
        self.setWindowTitle("多窗口交互(1)： 不使用信号与槽")

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton("弹出对话框1")
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton("弹出对话框2")
        self.button2.clicked.connect(self.onButton2Click)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)

        self.setLayout(gridLayout)

    def onButton1Click(self):
        dialog = DateDialog(self)
        result = dialog.exec()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        dialog.destroy()

    def onButton2Click(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result == QDialog.Accepted:
            print("点击确定按钮")
        else:
            print("点击取消按钮")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MultiWindow1()
    win.show()
    sys.exit(app.exec_())
