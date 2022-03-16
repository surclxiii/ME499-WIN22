#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QSlider, QLineEdit
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from random import random
import numpy as np
import digital_signal


class Grapher(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Grapher')
        self.textbox = QLineEdit(self)

        # Slider
        self.amp = 1000
        self.fre = 1000
        self.pha = 0
        sl_amp = QSlider(Qt.Horizontal)
        sl_amp.setRange(0, 5000)
        sl_fre = QSlider(Qt.Horizontal)
        sl_fre.setRange(0, 5000)
        sl_pha = QSlider(Qt.Horizontal)
        sl_pha.setRange(0, 5000)

        # Functions
        lab_amp = QLabel('Amplitude', self)
        sl_amp.valueChanged.connect(lambda: amp_slide())
        lab_amp.setBuddy(sl_amp)
        lab_fre = QLabel('Frequency', self)
        sl_fre.valueChanged.connect(lambda: freq_slide())
        lab_fre.setBuddy(sl_fre)
        lab_pha = QLabel('Phase shift', self)
        sl_pha.valueChanged.connect(lambda: phase_slide())
        lab_pha.setBuddy(sl_pha)

        # Quit buttons for the interface
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # Graph button
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
        left_side_layout.addWidget(quit_button)
        left_side_layout.addWidget(self.textbox)
        left_side_layout.addWidget(lab_amp)
        left_side_layout.addWidget(sl_amp)
        left_side_layout.addWidget(lab_fre)
        left_side_layout.addWidget(sl_fre)
        left_side_layout.addWidget(lab_pha)
        left_side_layout.addWidget(sl_pha)
        top_level_layout.addLayout(left_side_layout)
        top_level_layout.addWidget(self.display)

        def amp_slide():
            value = sl_amp.value()
            scale_value = value/1000
            lab_amp.setText("Amplitude: " + "%.3f" % scale_value)
            lab_amp.adjustSize()
            self.amp = sl_amp.value()

        def freq_slide():
            value = sl_fre.value()
            scale_value = value/1000
            lab_fre.setText("Frequency: " + "%.3f" % scale_value)
            lab_fre.adjustSize()
            self.fre = sl_fre.value()

        def phase_slide():
            value = sl_pha.value()
            scale_value = value/1000
            lab_pha.setText("Phase shift: " + "%.3f" % scale_value)
            lab_pha.adjustSize()
            self.pha = sl_pha.value()

    def graph(self):
        # fs = 1000
        # t = np.arange(-5, 5, 1 / fs)
        # x = (self.amp/1000) * np.sin(2 * np.pi * (self.fre/1000) * (t + (self.pha/1000)))
        # arr = [t, x]
        [data, samp_rate] = digital_signal.DigitalSignal.from_wav('starwars.wav')
        length = data.shape[0] / samp_rate
        time = np.linspace(0., length, data.shape[0])
        arr = [time, data]
        self.draw(time, data)

    def draw(self, arr):
        self.figure.clear()
        # ax = self.figure.add_subplot(111)
        # ax.plot(arr[0], arr[1])
        # ax.set_title(self.text)
        # ax.set_xlabel('x [rad]')
        # ax.set_ylabel('sin (x)')
        # ax.set_xlim([0, 5])
        # ax.set_ylim([-5, 5])
        plt.plot(arr[0], arr[:, 0], label="Left")
        plt.plot(arr[1], arr[:, 1], label="Right")
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
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

# Work with Ittiwat
