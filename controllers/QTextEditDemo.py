#! /usr/bin/python
# -*-coding:utf-8-*-
# Author: Tony
# Date: 2019/9/28 23:26
# Description:

import sys

from PyQt5.QtWidgets import *


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTextEdit控件演示")

        self.resize(300, 320)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton("显示文本")
        self.buttonHtml = QPushButton("显示HTML")

        self.buttonToText = QPushButton("获取文本")
        self.buttonToHtml = QPushButton("获取HTML")


        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonHtml)
        layout.addWidget(self.buttonToHtml)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHtml.clicked.connect(self.onClick_ButtonHtml)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHtml.clicked.connect(self.onClick_ButtonToHtml)

    def onClick_ButtonText(self):
        self.textEdit.setPlainText("Hello World, 世界你好吗？") # 设置纯文本

    def onClick_ButtonHtml(self):
        self.textEdit.setHtml('<font color="blue" size="5">Hello World</font>')  # 设置html

    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText()) # 获取纯文本

    def onClick_ButtonToHtml(self):
        print(self.textEdit.toHtml())  # 获取html


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())

