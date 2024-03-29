#! /usr/bin/python
# -*-coding:utf-8-*-
# Author: Tony
# Date: 2019/9/22 17:27
# Description:
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication类实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(300, 150)
    # 移动窗口
    w.move(300, 300)

    # 设置窗口的标题
    w.setWindowTitle("第一个基于PyQt5的桌面应用")
    # 显示窗口
    w.show()

    # 进入程序的主循环、并通过exit函数确保株循环安全结束
    sys.exit(app.exec_())
