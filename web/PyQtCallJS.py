#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/10 22:06 
@Description:  PyQt5调用JavaScript代码

PyQt5和JavaScript交互

什么叫交互

PyQt5  <-> JavaScript


"""

import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class PyQtCallJS(QWidget):

    def __init__(self):
        super(PyQtCallJS, self).__init__()
        self.setWindowTitle("PyQt5调用JavaScript代码")
        self.setGeometry(5, 30, 1355, 730)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.browser = QWebEngineView()

        url = os.getcwd() + "/tt.html"
        self.browser.load(QUrl.fromLocalFile(url))
        self.layout.addWidget(self.browser)

        button = QPushButton("设置全名")

        self.layout.addWidget(button)
        button.clicked.connect(self.fullname)

    def js_callback(self, result):
        print(result)

    def fullname(self):
        self.value = "hello world"
        self.browser.page().runJavaScript('fullname("' + self.value + '");', self.js_callback)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyQtCallJS()
    win.show()
    sys.exit(app.exec_())

