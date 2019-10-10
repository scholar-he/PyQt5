#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/10 21:30 
@Description:  使用线程类(QThread)编写计数器

QThread

def run(self)
    while True:
        self.sleep(1)
        if sec == 5:
            break

QLCDNumber

workThread(QThread)
用到自定义信号
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sec = 0


class WorkThread(QThread):
    timer = pyqtSignal()  # 每隔一秒发送一次信号
    end = pyqtSignal()  # 计数完成后发送一次信号
    def run(self):
        while True:
            self.sleep(1)  # 休眠一秒
            if sec == 5:
                self.end.emit()  # 发送end信号
                break
            self.timer.emit()  # 发送timer信号


class Counter(QWidget):
    def __init__(self):
        super(Counter, self).__init__()
        self.setWindowTitle("使用线程类(QThread)编写计数器")
        self.resize(300, 120)

        layout = QVBoxLayout()
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)

        button = QPushButton("开始计数")
        layout.addWidget(button)

        self.workThread = WorkThread()

        self.workThread.timer.connect(self.count)
        self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)

        self.setLayout(layout)

    def count(self):
        global sec
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self, "消息", "计数结果", QMessageBox.Ok)

    def work(self):
        self.workThread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Counter()
    main.show()
    sys.exit(app.exec_())
