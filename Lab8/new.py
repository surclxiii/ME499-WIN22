#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QSlider, QLineEdit
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class Grapher(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Grapher')

        self.textbox = QLineEdit(self)

        # Slider
        # Setting the initial value for amplitude, frequency and phase
        self.amplitude = 1000
        self.freq = 1000
        self.phase = 0

        # Creating sliders with range
        sl_amp = QSlider(Qt.Horizontal)
        sl_amp.setRange(0, 5000)
        sl_freq = QSlider(Qt.Horizontal)
        sl_freq.setRange(0, 5000)
        sl_phase = QSlider(Qt.Horizontal)
        sl_phase.setRange(0, 5000)

        # Creating labels and connect with the functions
        label_amp = QLabel('Amplitude', self)
        sl_amp.valueChanged.connect(lambda: change_amp())
        label_amp.setBuddy(sl_amp)
        label_freq = QLabel('Frequency', self)
        sl_freq.valueChanged.connect(lambda: change_freq())
        label_freq.setBuddy(label_freq)
        label_phase = QLabel('Phase', self)
        sl_phase.valueChanged.connect(lambda: change_phase())
        label_phase.setBuddy(sl_phase)

        # Quit button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # Graph button to create new graph
        graph_button = QPushButton('Graph')
        graph_button.clicked.connect(self.graph_t)
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

        left_side_layout.addWidget(self.textbox)
        left_side_layout.addWidget(quit_button)
        left_side_layout.addWidget(label_amp)
        left_side_layout.addWidget(sl_amp)
        left_side_layout.addWidget(label_freq)
        left_side_layout.addWidget(sl_freq)
        left_side_layout.addWidget(label_phase)
        left_side_layout.addWidget(sl_phase)
        top_level_layout.addLayout(left_side_layout)
        top_level_layout.addWidget(self.display)

        def change_amp():
            """
            displaying the value
            :return:
            """
            value = sl_amp.value()
            scale_value = value/1000
            label_amp.setText("Amplitude:" + "%.3f" % scale_value)
            label_amp.adjustSize()
            self.amplitude = sl_amp.value()

        def change_freq():
            """
            displaying the value
            :return:
            """
            value = sl_freq.value()
            scale_value = value/1000
            label_freq.setText("Frequency:" + "%.3f" % scale_value)
            label_freq.adjustSize()
            self.freq = sl_freq.value()

        def change_phase():
            """
            dis playing the value
            :return:
            """
            value = sl_phase.value()
            scale_value = value/1000
            label_phase.setText("Phase:" + "%.3f" % scale_value)
            label_phase.adjustSize()
            self.phase = sl_phase.value()

    def graph(self):
        fs = 1000
        t = np.arange(-5, 5, 1 / fs)
        x = (self.amplitude/1000) * np.sin(2 * np.pi * (self.freq/1000) * (t + (self.phase/1000)))
        data = [t, x]
        self.draw(data)

    def draw(self, data):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.plot(data[0], data[1])
        ax.set_title(self.text)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])

        self.display.draw()

    def graph_t(self):
        self.text = self.textbox.text()
        if self.text == '':
            self.text = 'Graph'


if __name__ == '__main__':
    app = QApplication([])

    gui = Grapher()

    gui.show()

    app.exec_()
