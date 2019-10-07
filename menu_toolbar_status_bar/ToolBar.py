#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/7 10:47 
@Description: 创建和使用工具栏

工具栏默认按钮：只显示图标，将文本作为悬停提示展示

工具栏按钮有三种显示状态

1. 只显示图标
2. 只显示文本
3. 同时显示图标和文本

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("工具栏案例")
        self.resize(300, 200)

        tb1 = self.addToolBar("File")

        new = QAction(QIcon("./images/ooopic.ico"), "new", self)
        tb1.addAction(new)

        open = QAction(QIcon("./images/ooopic1.ico"), "open", self)
        tb1.addAction(open)

        save = QAction(QIcon("./images/ooopic2.ico"), "save", self)
        tb1.addAction(save)

        # tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 设置文本在图标下方


        tb2 = self.addToolBar("File1")
        new1 = QAction(QIcon("./images/ooopic1.ico"), "新建", self)
        tb2.addAction(new1)
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 设置文本在图标下方

        tb1.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self, a):
        print("按下的工具栏按钮是", a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Toolbar()
    main.show()
    sys.exit(app.exec_())
