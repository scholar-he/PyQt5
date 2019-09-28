#! /usr/bin/python
# -*-coding:utf-8-*-
# Author: Tony
# Date: 2019/9/25 22:15
# Description: 使界面处于屏幕正中间

# QDesktopWidget

import sys
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):

    def __init__(self):
        super(CenterForm, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle("第一个主窗口的应用")

        # 设置窗口的尺寸
        self.resize(400, 300)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon("./images/music.ico"))

    main = CenterForm()
    main.show()

    sys.exit(app.exec_())