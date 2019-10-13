#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/13 22:08 
@Description:  设置伸缩量(addStretch)

"""
import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QApplication


class Stretch(QWidget):

    def __init__(self):
        super(Stretch, self).__init__()
        self.setWindowTitle("设置伸缩量")
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn1.setText("按钮1")
        btn2.setText("按钮2")
        btn3.setText("按钮3")

        layout = QHBoxLayout()

        layout.addStretch(1)
        layout.addWidget(btn1)

        layout.addStretch(2)
        layout.addWidget(btn2)

        layout.addStretch(3)
        layout.addWidget(btn3)


        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Stretch()
    win.show()
    sys.exit(app.exec_())
