#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/20 20:34 
@Description:  QSS子控件选择器

QComboBox
"""

import sys

from PyQt5.QtWidgets import *


class QSSSubControl(QWidget):

    def __init__(self):
        super(QSSSubControl, self).__init__()
        self.setWindowTitle("QSS子控件选择器")
        combo = QComboBox(self)
        combo.setObjectName("myComboBox")
        combo.addItem("window")
        combo.addItem("Linux")
        combo.addItem("Mac OS X")

        combo.move(50, 50)

        self.setGeometry(250, 200, 320, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QSSSubControl()
    # 选择器
    qssStyle = """
        QComboBox#myComboBox::drop-down {
            image:url(./images/gaoyuanyuan.jpg)
        }
    """
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec_())
