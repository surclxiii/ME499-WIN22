#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('I am an example window')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)

        # A layout
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Label
        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)

        # Slider
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 10)
        self.slider.valueChanged.connect(self.slidechange)

        # A button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # Add things to the layout
        layout.addWidget(self.slider)  # Label
        layout.addWidget(quit_button)

    def slidechange(self, value):
        self.label.setText(str(value))  # Change value


if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()
