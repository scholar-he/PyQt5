#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/11 22:09 
@Description:
"""
from PyQt5.QtCore import *


class Factorial(QObject):
    @pyqtSlot(int, result=int)
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return self.factorial(n-1) * n


if __name__ == '__main__':
    f = Factorial()
    res = f.factorial(4)
    print(res)