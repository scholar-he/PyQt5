#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/7 20:09 
@Description: 显示列表数据(QListView控件)

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel

class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.setWindowTitle("QListView案例")
        self.resize(300, 270)
        layout = QVBoxLayout()

        listview = QListView()

        listModel = QStringListModel()
        self.list = ["列表项1", "列表项2", "列表项3"]

        listModel.setStringList(self.list)

        listview.setModel(listModel)
        
        listview.clicked.connect(self.clicked)

        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, "QListView", "您选择了：" + self.list[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())

