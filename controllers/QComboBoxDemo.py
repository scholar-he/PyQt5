#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/5 20:08 
@Description: 下拉列表控件(QCombobox)

1. 如何将列表项添加到QCombox控件中

2. 如何获取选中的列表项
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件演示")
        self.resize(300, 100)

        layout = QVBoxLayout()

        self.label = QLabel("请选择编程语言")

        self.cb = QComboBox()
        self.cb.addItem("C++")
        self.cb.addItem("Python")
        self.cb.addItems(["Java", "C#", "Rubby"])

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChange(self, i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            print("item" + str(count) + "=" + self.cb.itemText(count))
        print("current index", i, "selection Changed", self.cb.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())

