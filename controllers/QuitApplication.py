#! /usr/bin/python
# -*-coding:utf-8-*-
# Author: Tony
# Date: 2019/9/25 22:23
# Description:

import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle("退出应用程序")

        # 添加Button
        self.button1 = QPushButton("退出应用程序")
        # 将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        # 通过sender获取button对象
        # sender = self.sender()
        # print(sender.text() + "按钮按下")
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())