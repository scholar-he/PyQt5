#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/9 21:28 
@Description:  QTreeView控件与系统定制模式

QTreeWidget

Model

QDirModel
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)

    tree.setWindowTitle("QTreeView")
    tree.resize(600, 400)

    tree.show()

    sys.exit(app.exec_())
