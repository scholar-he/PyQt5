#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/9 22:23 
@Description: 停靠控件(QDockWidget)

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DockDemo(QMainWindow):
    def __init__(self):
        super(DockDemo, self).__init__()

        self.setWindowTitle("停靠控件(QDockWidget)")

        layout = QHBoxLayout()
        self.items = QDockWidget("DockWidget", self)
        self.list = QListWidget()
        self.list.addItem("item1")
        self.list.addItem("item2")
        self.list.addItem("item3")

        self.items.setWidget(self.list)

        self.setCentralWidget(QLineEdit())

        self.items.setFloating(True)

        self.addDockWidget(Qt.RightDockWidgetArea, self.items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DockDemo()
    win.show()
    sys.exit(app.exec_())
