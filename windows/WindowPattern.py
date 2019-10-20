#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/20 16:41 
@Description:  设置窗口样式

"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class WindowPattern(QMainWindow):

    def __init__(self):
        super(WindowPattern, self).__init__()
        self.setWindowTitle("设置窗口的样式")
        self.resize(500, 260)

        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(images/gaoyuanyuan.jpg);}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowPattern()
    win.show()
    sys.exit(app.exec_())
