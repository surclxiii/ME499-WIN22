#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class SliderDisplay(QWidget):
    def __init__(self, name, low, high, ticks=1000, units=''):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Your code goes in here

    def value(self):
        """Return the current value of the slider"""
        return 0


if __name__ == '__main__':
    app = QApplication([])

    slider = SliderDisplay('foo', 0, 1)

    slider.show()

    app.exec_()

