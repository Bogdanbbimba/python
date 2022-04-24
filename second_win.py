# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale

class TestWin(QWidget):
    def __init__(self):
        pass

    def timer_test(self):
        self.timer = QTime(0, 1, 0)
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)


    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times', 36, QFont.bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def connects(self):
        self.btn_test1.clicked.connect(self.timer_test)