#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/7 11:15 
@Description:  使用打印机


"""
import sys

from PyQt5 import QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextEdit, QApplication


class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport, self).__init__()
        self.setGeometry(500, 200, 300, 300)
        self.button = QPushButton("打印QTextEdit控件的内容", self)

        self.button.setGeometry(20, 20, 260, 30)
        self.editor = QTextEdit("默认文本", self)
        self.editor.setGeometry(20, 60, 260, 200)

        self.button.clicked.connect(self.print)


    def print(self):
        printer = QtPrintSupport.QPrinter()

        painter = QtGui.QPainter()
        painter.begin(printer)  # 将绘制的目标重定向到打印机
        screen = self.editor.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()
        print("print")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PrintSupport()
    main.show()
    sys.exit(app.exec_())
