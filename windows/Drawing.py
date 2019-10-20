#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/20 17:09 
@Description:  项目实战: 实现绘图应用

三个核心问题
1. 如何绘图

    在paintEvent方法中绘图，通过update方法调用paintEvent事件

2. 在哪里绘图

    在白色背景的QPixmap对象中绘图

3. 如何通过鼠标移动进行绘图

鼠标拥有三个事件：
    1）鼠标按下  mousePressEvent
    2）鼠标移动  mouseMoveEvent
    3）鼠标抬起  mouseReleaseEvent

"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Drawing(QWidget):

    def __init__(self):
        super(Drawing, self).__init__()
        self.setWindowTitle("绘图应用")

        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()

    def initUI(self):
        self.resize(600, 600)
        # 画布大小为400*400，背景为白色
        self.pix = QPixmap(600, 600)
        self.pix.fill(Qt.white)

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        # 根据鼠标指针前后两个位置绘制直线
        pp.drawLine(self.lastPoint, self.endPoint)
        # 让前一个坐标值等于后一个坐标值
        # 这样就能画出连续的线
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton:
            self.lastPoint = QMouseEvent.pos()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.endPoint = QMouseEvent.pos()
            self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标左键释放
        if QMouseEvent.button() == Qt.LeftButton:
            self.endPoint = QMouseEvent.pos()
            # 进行重新绘制
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Drawing()
    win.show()
    sys.exit(app.exec_())

