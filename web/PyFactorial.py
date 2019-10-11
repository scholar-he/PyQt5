#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/11 21:51 
@Description:

JavaScript调用Python函数计算阶乘

将Python的一个对象映射到JavaScript中

将槽函数映射到JavaScript中


"""
import os
import sys

from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from factorial import *

channel = QWebChannel()
factorial = Factorial()

class PyFactorail(QWidget):

    def __init__(self):
        super(PyFactorail, self).__init__()
        self.setWindowTitle("Python计算阶乘")
        self.resize(600, 300)
        layout = QVBoxLayout()

        self.browser = QWebEngineView()
        url = os.getcwd() + "./f.html"
        self.browser.load(QUrl.fromLocalFile(url))
        channel.registerObject("obj", factorial)
        self.browser.page().setWebChannel(channel)

        layout.addWidget(self.browser)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyFactorail()
    win.show()
    sys.exit(app.exec_())
