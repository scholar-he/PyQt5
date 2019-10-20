#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/20 17:30 
@Description:  QSS基础

QSS (Qt Style Sheet)
Qt样式表

用于设置控件的样式

CSS

"""

import sys

from PyQt5.QtWidgets import *


class BasicQSS(QWidget):

    def __init__(self):
        super(BasicQSS, self).__init__()
        self.setWindowTitle("QSS样式")
        btn1 = QPushButton(self)
        btn1.setText("按钮1")

        btn2 = QPushButton(self)
        btn2.setText("按钮2")

        btn3 = QPushButton(self)
        btn3.setText("按钮3")

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BasicQSS()
    # 选择器
    qssStyle = """
        QPushButton {
            background-color: red
        }
    """
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec_())
