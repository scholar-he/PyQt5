#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/20 16:00 
@Description:
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DateDialog(QDialog):

    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle("DateDialog")

        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit()
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent=None):
        dialog = DateDialog(parent)
        result = dialog.exec()
        date = dialog.dateTime()
        return (date.date(), date.time(), result==QDialog.Accepted)

