#! /usr/bin/python
# -*-coding:utf-8-*-
# Author: Tony
# Date: 2019/9/28 18:14
# Description: 显示控件提示信息

import sys

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QPushButton, QHBoxLayout, QMainWindow


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置字体
        QToolTip.setFont(QFont("SansSerif", 12))
        self.setToolTip("今天是<b>星期六</b>")
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("设置控件提示信息")

        self.button = QPushButton("我的按钮")
        self.button.setToolTip("这是一个按钮")
        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/ooopic1.ico"))
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())