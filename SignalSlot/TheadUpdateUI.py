#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/16 22:17 
@Description:  多线程更新UI数据(在两个线程中传递数据)
"""

import sys
import time

from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime


class BackendThread(QThread):

    update_date = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))
            time.sleep(1)


class ThreadUpdateUI(QDialog):

    def __init__(self):
        super(ThreadUpdateUI, self).__init__()
        self.setWindowTitle("多线程更新UI数据")
        self.resize(400, 100)
        self.input = QLineEdit(self)
        self.input.resize(400, 100)

        self.initUI()

    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)

        self.backend.start()

    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ThreadUpdateUI()
    win.show()
    sys.exit(app.exec_())
