#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QSlider, QLineEdit
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from random import random
import numpy as np



class GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('GUI')
        self.textbox = QLineEdit(self)
    # Slider
        sl_low = QSlider(Qt.Horizontal)
        sl_low.setRange(0, 2000)
        sl_high = QSlider(Qt.Horizontal)
        sl_high.setRange(0, 2000)
    # Label
        lab_low = QLabel('Low: ', self)
        #sl_low.valueChanged.connect(lambda: low_slide())
        lab_high = QLabel('High: ', self)
        #sl_high.valueChanged.connect(lambda: high_slide())
        lab_start = QLabel('Start: ', self)
        lab_end = QLabel('End: ', self)
        lab_load = QLabel('Load file: ', self)
        lab_save = QLabel('Save file: ', self)
    # Button
        reset_button = QPushButton('Reset all')
        #reset_button.clicked.connect()
        load_button = QPushButton('Load')
        #load_button.clicked.connect()
        save_button = QPushButton('Save')
        #save_button.clicked.connect()

    # Display Plot
        self.figure = Figure()
        self.display = FigureCanvas(self.figure)
        self.figure.clear()

    # Layout
        widget = QWidget()
        self.setCentralWidget(widget)
        top_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        widget.setLayout(top_layout)
        top_layout.addLayout(left_layout)
        top_layout.addWidget(self.display)
        top_layout.addLayout(right_layout)
        left_layout.addWidget(lab_low)
        left_layout.addWidget(sl_low)
        left_layout.addWidget(lab_high)
        left_layout.addWidget(sl_high)
        right_layout.addWidget(lab_start)
        right_layout.addWidget(lab_end)
        right_layout.addWidget(reset_button)
        left_layout.addWidget(lab_load)
        left_layout.addWidget(load_button)
        left_layout.addWidget(lab_save)
        left_layout.addWidget(save_button)

if __name__ == '__main__':
    app = QApplication([])

    gui = GUI()

    gui.show()

    app.exec_()
