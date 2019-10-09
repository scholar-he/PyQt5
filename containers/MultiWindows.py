#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/9 22:31 
@Description:  容纳多文档的窗口

QMdiArea

QMdiSubWindow

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MutilWindows(QMainWindow):

    count = 0

    def __init__(self):
        super(MutilWindows, self).__init__()
        self.setWindowTitle("容纳多文档的窗口")

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")

        file.triggered.connect(self.windowaction)

    def windowaction(self, q):
        if q.text() == "New":
            MutilWindows.count += 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(MutilWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        elif q.text() == "Titled":
            self.mdi.tileSubWindows()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MutilWindows()
    win.show()
    sys.exit(app.exec_())