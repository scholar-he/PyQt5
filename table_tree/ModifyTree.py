#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/9 21:09 
@Description:  添加、修改和删除树控件中的节点
"""
import sys

from PyQt5.QtWidgets import *


class ModifyTree(QWidget):
    def __init__(self):
        super(ModifyTree, self).__init__()
        self.setWindowTitle("TreeWidget案例")

        operatorLayout = QHBoxLayout()
        addBtn = QPushButton("添加节点")
        updateBtn = QPushButton("修改节点")
        deleteBtn = QPushButton("删除节点")

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

        self.tree = QTreeWidget()

        self.tree.setColumnCount(2)

        self.tree.setHeaderLabels(["key", "value"])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, "root")
        root.setText(1, "0")

        child1 = QTreeWidgetItem(root)
        child1.setText(0, "child1")
        child1.setText(1, "1")

        child2 = QTreeWidgetItem(root)
        child2.setText(0, "child2")
        child2.setText(1, "2")

        child3 = QTreeWidgetItem(root)
        child3.setText(0, "child3")
        child3.setText(1, "3")

        self.tree.clicked.connect(self.onTreeClicked)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)

        self.setLayout(mainLayout)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print("key=%s, value=%s" % (item.text(0), item.text(1)))

    # 添加节点
    def addNode(self):
        print("添加节点")
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0, "新节点")
        node.setText(1, "新值")

    # 修改节点
    def updateNode(self):
        print("修改节点")
        item = self.tree.currentItem()
        item.setText(0, "修改节点")
        item.setText(1, "值已被修改")

    def deleteNode(self):
        print("删除节点")
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ModifyTree()
    win.show()
    sys.exit(app.exec_())
