#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/6 20:32 
@Description: 输入各种风格的日期和时间

QDateTimeEdit
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DateTimeEdit1(QWidget):
    def __init__(self):
        super(DateTimeEdit1, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 90)
        self.setWindowTitle("设置不同风格的日期和时间")

        layout = QVBoxLayout()
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())

        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit2.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateTimeEdit = dateTimeEdit1

        dateTimeEdit2.setCalendarPopup(True)  # 设置成日历风格

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")

        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")

        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)


        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)

        self.btn = QPushButton("获取日期和时间")
        self.btn.clicked.connect(self.onButtonClick)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    # 日期变换
    def onDateChanged(self, date):
        print(date)

    # 时间变换
    def onTimeChanged(self, time):
        print(time)

    # 日期和时间变换
    def onDateTimeChanged(self, datetime):
        print(datetime)

    def onButtonClick(self):
        dateTime = self.dateTimeEdit.dateTime()
        print(dateTime)

        # 最大日期
        print(self.dateTimeEdit.maximumDate())
        # 最大日期和时间
        print(self.dateTimeEdit.maximumDateTime())

        # 最小日期
        print(self.dateTimeEdit.minimumDate())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DateTimeEdit1()
    main.show()
    sys.exit(app.exec_())
