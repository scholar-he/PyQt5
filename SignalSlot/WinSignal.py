#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/16 21:51 
@Description:  为窗口类添加信号

"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WinSignal(QWidget):

    button_clicked_signal = pyqtSignal()

    def __init__(self):
        super(WinSignal, self).__init__()
        self.setWindowTitle("为窗口添加信号")
        self.resize(300, 100)

        btn = QPushButton("关闭窗口", self)

        btn.clicked.connect(self.btn_clicked)

        self.button_clicked_signal.connect(self.btn_close)

    def btn_clicked(self):
        self.button_clicked_signal.emit()

    def btn_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinSignal()
    win.show()
    sys.exit(app.exec_())
