#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/7 20:25 
@Description:  扩展的列表控件(QListWidget)

QListView
"""

import sys
from PyQt5.QtWidgets import *

class ListWidgetDemo(QMainWindow):
    def __init__(self):
        super(ListWidgetDemo, self).__init__()
        self.setWindowTitle("QListWidget案例")
        self.resize(300, 270)
        self.listWidget = QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        self.listWidget.addItem("item4")
        self.listWidget.addItem("item5")

        self.listWidget.itemClicked.connect(self.clicked)

        self.setCentralWidget(self.listWidget)

    def clicked(self, item):
        print(item.text())
        QMessageBox.information(self, "QListWidget", "您选择了：" + item.text())  # 两种方法获取选择项的信息都可以
        # QMessageBox.information(self, "QListWidget", "您选择了：" + self.listWidget.item(self.listWidget.row(item)).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ListWidgetDemo()
    win.show()
    sys.exit(app.exec_())
