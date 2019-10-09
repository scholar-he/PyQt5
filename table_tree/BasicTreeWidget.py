#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/9 20:46 
@Description:  树控件(QTreeWidget)的用法
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class BasicTreeWidget(QMainWindow):
    def __init__(self):
        super(BasicTreeWidget, self).__init__()
        self.setWindowTitle("树控件(QTreeWisget)的基本用法")

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)

        # 指定列标签
        self.tree.setHeaderLabels(["key", "value"])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, "根节点")
        root.setIcon(0, QIcon("./images/ooopic.ico"))
        self.tree.setColumnWidth(0, 120)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, "子节点1")
        child1.setText(1, "子节点1的数据")
        child1.setIcon(0, QIcon("./images/ooopic1.ico"))
        child1.setCheckState(0, Qt.Checked)

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, "子节点")
        child2.setIcon(0, QIcon("./images/ooopic2.ico"))


        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, "子节点2-1")
        child3.setText(1, "新的值")
        child3.setIcon(0, QIcon("./images/ooopic.ico"))

        self.tree.expandAll()

        self.setCentralWidget(self.tree)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BasicTreeWidget()
    win.show()
    sys.exit(app.exec_())
