#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/20 15:51 
@Description: Override (覆盖) 槽函数

"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class OverrideSlot(QWidget):

    def __init__(self):
        super(OverrideSlot, self).__init__()
        self.setWindowTitle("Override(覆盖)槽函数")

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()
        elif QKeyEvent.key() == Qt.Key_Alt:
            self.setWindowTitle("按下Alt键")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = OverrideSlot()
    win.show()
    sys.exit(app.exec_())
