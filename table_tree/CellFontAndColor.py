#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/8 21:32 
@Description:  设置单元格字体和颜色

"""

import sys
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QApplication
from PyQt5.QtGui import QBrush, QColor, QFont


class CellFontAndColor(QWidget):
    def __init__(self):
        super(CellFontAndColor, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格字体和颜色")
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        tableWidget.setHorizontalHeaderLabels(["姓名", "性别", "体重（kg）"])

        newItem = QTableWidgetItem("雷神")
        newItem.setFont(QFont("Times", 14, QFont.Black))

        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("女神")
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("160")
        newItem.setFont(QFont("Times", 20, QFont.Black))
        newItem.setForeground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 2, newItem)

        layout.addWidget(tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CellFontAndColor()
    win.show()
    sys.exit(app.exec_())
