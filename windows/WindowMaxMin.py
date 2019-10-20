#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/20 16:53 
@Description:
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class WindowMaxMin(QWidget):

    def __init__(self):
        super(WindowMaxMin, self).__init__()
        self.resize(300, 400)
        self.setWindowTitle("用代码控制窗口的最大化和最小化")
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        layout = QVBoxLayout()
        maxButton1 = QPushButton()
        maxButton1.setText("窗口最大化1")
        maxButton1.clicked.connect(self.maxmized1)

        maxButton2 = QPushButton()
        maxButton2.setText("窗口最大化2")
        maxButton2.clicked.connect(self.showMaximized)

        minButton = QPushButton()
        minButton.setText("窗口最小化")
        minButton.clicked.connect(self.showMinimized)

        layout.addWidget(maxButton1)
        layout.addWidget(maxButton2)
        layout.addWidget(minButton)

        self.setLayout(layout)

    def maxmized1(self):
        desktop = QApplication.desktop()
        # 获取桌面可用尺寸
        rect = desktop.availableGeometry()
        self.setGeometry(rect)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowMaxMin()
    win.show()
    sys.exit(app.exec_())
