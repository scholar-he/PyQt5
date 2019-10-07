#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/7 21:41 
@Description:  在单元格中放置控件

setItem: 将文本放入单元格里
setCellWidget: 将控件放到单元格里
setStyleSheet: 设置控件的样式(QSS)
"""
import sys
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem,\
    QHBoxLayout, QApplication, QComboBox, QPushButton


class PlaceControlCell(QWidget):
    def __init__(self):
        super(PlaceControlCell, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中放置控件")
        self.resize(430, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()

        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(["姓名", "性别", "体重(kg)"])
        textItem = QTableWidgetItem("小明")
        tableWidget.setItem(0, 0, textItem)

        combox = QComboBox()
        combox.addItem("男")
        combox.addItem("女")
        # QSS Qt StyleSheet
        combox.setStyleSheet("QComboBox{margin:3px}")
        tableWidget.setCellWidget(0, 1, combox)

        modifyButton = QPushButton("修改")
        modifyButton.setDown(True)
        modifyButton.setStyleSheet("QPushButton{margin:3px}")
        tableWidget.setCellWidget(0, 2, modifyButton)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PlaceControlCell()
    win.show()
    sys.exit(app.exec_())
