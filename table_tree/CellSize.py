#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/8 22:16 
@Description:  设置单元格尺寸

"""

import sys
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QApplication
from PyQt5.QtGui import QBrush, QColor, QFont


class CellSize(QWidget):
    def __init__(self):
        super(CellSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格字体和颜色")
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        tableWidget.setHorizontalHeaderLabels(["姓名", "性别", "体重（kg）"])

        tableWidget.setRowHeight(0, 80)
        tableWidget.setColumnWidth(2, 140)

        newItem = QTableWidgetItem("雷神")
        newItem.setFont(QFont("Times", 30, QFont.Black))

        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("女神")
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("160")
        newItem.setFont(QFont("Times", 60, QFont.Black))
        newItem.setForeground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 2, newItem)

        layout.addWidget(tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CellSize()
    win.show()
    sys.exit(app.exec_())
