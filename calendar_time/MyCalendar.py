#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/6 16:01 
@Description: 日历控件

QCalendarWidget

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988, 1, 1))
        self.cal.setMaximumDate(QDate(2088, 1, 1))

        self.cal.setGridVisible(True)  # 加可视化网格
        self.cal.move(20, 20)
        self.resize(400, 350)
        self.setWindowTitle("日历演示")
        self.cal.clicked.connect(self.showDate)

        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.move(20, 300)

    def showDate(self, date):
        # self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.label.setText(self.cal.selectedDate().toString("yyyy-MM-dd dddd"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec_())