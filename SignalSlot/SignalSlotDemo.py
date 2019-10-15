#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/15 22:58 
@Description:  信号(Signal) 与槽(slot)

"""
import sys

from PyQt5.QtWidgets import *


class SignalSlotDemo(QWidget):

    def __init__(self):
        super(SignalSlotDemo, self).__init__()
        self.initUI()

    def onClick(self):
        self.btn.setText("信号已经发出")
        self.btn.setStyleSheet("QPushButton(max-width:200px;min-width:200px)")

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("信号(Signal) 与槽(slot)")
        self.btn = QPushButton("我的按钮", self)
        self.btn.clicked.connect(self.onClick)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SignalSlotDemo()
    win.show()
    sys.exit(app.exec_())
