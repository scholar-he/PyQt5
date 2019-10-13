#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/13 22:53 
@Description: 拖动控件之间的边界(QSplitter)

"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class Splitter(QWidget):

    def __init__(self):
        super(Splitter, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QSplitter案例")
        self.setGeometry(300, 300, 300, 300)

        hbox = QHBoxLayout()

        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textedit)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Splitter()
    win.show()
    sys.exit(app.exec_())



