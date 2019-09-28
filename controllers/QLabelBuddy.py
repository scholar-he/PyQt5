#! /usr/bin/python
# -*-coding:utf-8-*-
# Author: Tony
# Date: 2019/9/28 19:06
# Description:

"""
QLabel与伙伴关系
mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
mainLayout.addWidget(控件对象, rowIndex, columnIndex, row, column)

"""
import sys

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication


class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Qlabel与伙伴关系")

        nameLabel = QLabel("&Name", self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴关系
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel("&Password", self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴关系
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton("&OK")
        btnCancel = QPushButton("&Cancel")

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())