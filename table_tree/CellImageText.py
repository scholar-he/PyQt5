#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/8 22:23 
@Description:  在单元格中实现图文混排的效果

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class CellImageText(QWidget):
    def __init__(self):
        super(CellImageText, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中实现图文混排的效果")
        self.resize(500, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(4)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(["姓名", "性别", "体重", "显示图片"])

        newItem = QTableWidgetItem("李宁")
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("男")
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("160")
        tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem(QIcon("./images/jiajingwen.jpg"), "贾静雯")
        tableWidget.setItem(0, 3, newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CellImageText()
    win.show()
    sys.exit(app.exec_())

