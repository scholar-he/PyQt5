#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/5 21:08 
@Description: 计数器控件(QSpinBox)

"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QSpinbox演示")
        self.resize(300, 100)

        self.label = QLabel("当前值")
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.sb = QSpinBox()
        layout.addWidget(self.sb)
        # self.sb.setMaximum(18) # 设置最大值
        self.sb.setRange(10, 20)  # 设置区间
        self.sb.setSingleStep(2)  # 设置步长
        self.sb.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        self.label.setText("当前值： " + str(self.sb.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())
