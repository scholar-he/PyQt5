#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/6 12:15 
@Description: 绘制不同类型的直线

"""

import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle("设置Pen的样式")

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.red, 3, Qt.SolidLine)

        painter.setPen(pen)
        painter.drawLine(20, 40, 280, 40)

        pen.setStyle(Qt.DashLine)  # 虚线
        painter.setPen(pen)
        painter.drawLine(20, 60, 280, 60)

        pen.setStyle(Qt.DashDotLine)  # 点划线
        painter.setPen(pen)
        painter.drawLine(20, 80, 280, 80)

        pen.setStyle(Qt.DashDotDotLine) # 双点划线
        painter.setPen(pen)
        painter.drawLine(20, 100, 280, 100)

        pen.setStyle(Qt.DotLine)  # 单点线
        painter.setPen(pen)
        painter.drawLine(20, 120, 280, 120)

        pen.setStyle(Qt.CustomDashLine)  # 自定义线条样式
        pen.setDashPattern([1, 10, 5, 8])
        painter.setPen(pen)
        painter.drawLine(20, 140, 280, 140)

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())
