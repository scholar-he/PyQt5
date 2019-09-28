#! /usr/bin/python
# -*-coding:utf-8-*-
# Author: Tony
# Date: 2019/9/28 17:46
# Description:

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow ,QApplication

"""
窗口的setWindowIcon方法用于设置窗口的图标，只在widows中可用

QApplication中的setWindowIcon方法用于设置主窗口的图标和应用程序的图标，但调用了
窗口的setwWindowIcon方法，QApplication中的setWindowIcon方法就只能用于设置应用程序图标了
"""


class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 250)
        # 设置窗口的主题
        self.setWindowTitle("设置窗口图标")
        # 设置窗口图标
        self.setWindowIcon(QIcon("./images/ooopic.ico"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/matte.ico"))
    main = IconForm()
    main.show()
    sys.exit(app.exec_())