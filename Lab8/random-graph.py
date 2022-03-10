#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from random import random


class Grapher(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Grapher')

        # Control buttons for the interface
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        graph_button = QPushButton('Graph')
        graph_button.clicked.connect(self.graph)

        # The display for the graph
        self.figure = Figure()
        self.display = FigureCanvas(self.figure)
        self.figure.clear()

        # The layout of the interface
        widget = QWidget()
        self.setCentralWidget(widget)

        top_level_layout = QHBoxLayout()
        widget.setLayout(top_level_layout)
        left_side_layout = QVBoxLayout()

        left_side_layout.addWidget(graph_button)
        left_side_layout.addStretch()
        left_side_layout.addWidget(quit_button)

        top_level_layout.addLayout(left_side_layout)
        top_level_layout.addWidget(self.display)

    def graph(self):
        self.draw([random() for i in range(25)])

    def draw(self, data):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.plot(data)
        ax.set_title('Graph')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        self.display.draw()


if __name__ == '__main__':
    app = QApplication([])

    gui = Grapher()

    gui.show()

    app.exec_()