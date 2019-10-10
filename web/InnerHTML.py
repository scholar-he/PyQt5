#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/10 22:02 
@Description:  显示嵌入Web页面

"""

import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class InnerHTMl(QMainWindow):

    def __init__(self):
        super(InnerHTMl, self).__init__()
        self.setWindowTitle("显示嵌入Web页面")
        self.setGeometry(5, 50, 1335, 730)

        self.browser = QWebEngineView()
        self.browser.setHtml("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>测试页面</title>
        </head>
        <body>
            <h1>Hello PyQt5</h1>
            <h2>Hello PyQt5</h2>
            <h3>Hello PyQt5</h3>
        </body>
        </html>
        """)
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = InnerHTMl()
    win.show()
    sys.exit(app.exec_())
