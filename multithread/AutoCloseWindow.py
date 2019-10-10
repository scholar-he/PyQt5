#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/10 21:22 
@Description:  让程序定时关闭

QTimer.singleShot
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel("<font color=red size=140><b>Hello Word，窗口"
                  "在5秒后自动关闭</b></font>")
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)  # 隐藏窗口标题栏
    label.show()
    QTimer.singleShot(5000, app.quit)
    sys.exit(app.exec_())

