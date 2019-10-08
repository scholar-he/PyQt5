#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/8 22:32 
@Description:  改变单元格中图片的尺寸

setIconSize(QSize(width, height))
"""

import sys
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CellImageSize(QWidget):
    def __init__(self):
        super(CellImageSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("改变单元格中图片的尺寸")
        self.resize(650, 680)
        layout = QHBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setIconSize(QSize(200, 200))
        tableWidget.setColumnCount(3)
        tableWidget.setRowCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(["图片1", "图片2", "图片3"])

        # 让列的宽度和图片宽度相同
        for i in range(3):
            tableWidget.setColumnWidth(i, 200)

        # 让行的高度和图片高度相等
        for i in range(3):
            tableWidget.setRowHeight(i, 200)

        for k in range(9):
            i = k / 3  # 行
            j = k % 3  # 列
            newItem = QTableWidgetItem()
            newItem.setIcon(QIcon("./images/jiajingwen.jpg"))
            tableWidget.setItem(i, j, newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CellImageSize()
    win.show()
    sys.exit(app.exec_())

