#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/13 22:49 
@Description:  表单布局(QFormLayout)

"""

import sys

from PyQt5.QtWidgets import *


class FormForm(QWidget):

    def __init__(self):
        super(FormForm, self).__init__()
        self.setWindowTitle("表单布局")
        self.resize(350, 300)

        formLayout = QFormLayout()

        titleLabel = QLabel("标题")
        authorLabel = QLabel("作者")
        contentLabel = QLabel("内容")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        formLayout.addRow(titleLabel, titleEdit)
        formLayout.addRow(authorLabel, authorEdit)
        formLayout.addRow(contentLabel,contentEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FormForm()
    win.show()
    sys.exit(app.exec_())

