#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/16 22:29 
@Description:  信号与槽自动连接

on_onjectname_signalname

on_okButton_clicked()
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5 import QtCore


class AutoSignalSlot(QWidget):

    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.okButton = QPushButton("ok")
        self.okButton.setObjectName("okButton")
        self.okButton1 = QPushButton("cancel")
        self.okButton1.setObjectName("cancelButton")
        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        layout.addWidget(self.okButton1)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.okButton.clicked.connect(self.on_okButton_clicked)

    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print("点击了OK按钮")

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print("点击了cancel按钮")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AutoSignalSlot()
    win.show()
    sys.exit(app.exec_())

