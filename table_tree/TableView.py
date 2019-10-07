#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/7 11:44 
@Description:  显示二维表数据(QTableView控件)

数据源

Model

需要创建QTableView实例和一个数据源(Model), 然后将两者关联

MVC: Model  Viewer  Controller

MVC的目的是将后端的数据的前端页面的耦合度降低
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class TableView(QWidget):
    def __init__(self):
        super(TableView, self).__init__()
        self.setWindowTitle("QTableView表格视图控件演示")
        self.resize(500, 300)

        # 创建模型（4行3列）
        self.model = QStandardItemModel(4, 3)
        # 添加水平方向的字段
        self.model.setHorizontalHeaderLabels(["id", "姓名", "年龄"])

        self.tableview = QTableView()
        # 关联QTableView控件和Model
        self.tableview.setModel(self.model)

        # 添加数据
        item11 = QStandardItem("10")
        item12 = QStandardItem("雷神")
        item13 = QStandardItem("2000")
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)

        item31 = QStandardItem("30")
        item32 = QStandardItem("女神")
        item33 = QStandardItem("3000")
        self.model.setItem(2, 0, item31)
        self.model.setItem(2, 1, item32)
        self.model.setItem(2, 2, item33)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableView()
    main.show()
    sys.exit(app.exec_())
