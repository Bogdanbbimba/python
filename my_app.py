# напиши здесь код основного приложения и первого эк
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime 

from instr import *
from second_win import *


class MainWin(QWidget):
    def __init__(self):
        super.__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)        
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin(QWidget)

app = QApplication([])
win = MainWin()
win.show()
app.exec_()
