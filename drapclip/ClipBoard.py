#! /usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: Tony 2513141027
@Date: 2019/10/6 13:16 
@Description: 使用剪贴板


"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()

        self.setWindowTitle("剪贴板演示")

        textCopyButton = QPushButton("复制文本")
        textPasteButton = QPushButton("粘贴文本")

        htmlCopyButton = QPushButton("复制HTML")
        htmlPasteButton = QPushButton("粘贴HTML")

        imageCopyButton = QPushButton("复制图像")
        imagePasteButton = QPushButton("粘贴图像")

        self.textLabel = QLabel("默认文本")
        self.imageLabel = QLabel()
        # self.imageLabel.setPixmap(QPixmap("./images/gaoyuanyuan.jpg"))

        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(htmlCopyButton, 0, 1)
        layout.addWidget(imageCopyButton, 0, 2)
        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(htmlPasteButton, 1, 1)
        layout.addWidget(imagePasteButton, 1, 2)

        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)

        self.setLayout(layout)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("hello world")

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyHtml(self):
        mimeDate = QMimeData()
        mimeDate.setHtml("<b>Bold and <font color=red>Red</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeDate)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap("./images/jiajingwen.jpg").scaled(400, 400, aspectRatioMode=Qt.KeepAspectRatio)) # 保持图片原始比例

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())
