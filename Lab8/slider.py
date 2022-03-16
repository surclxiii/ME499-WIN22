#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class SliderDisplay(QWidget):
    def __init__(self, name, low, high, ticks=1000, units=''):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Your code goes in here
        label = QLabel(name, self)  # Create label with name
        slider = QSlider(Qt.Horizontal)  # Creat slider
        slider.setRange(low * ticks, high * ticks)  # Set range
        layout.addWidget(slider)  # Show slider
        slider.valueChanged.connect(lambda: sliderchange())

        def sliderchange():
            slider_val = slider.value()
            scaled = slider_val / ticks
            label.setText(name + ":" + "%.3f" % scaled + " " + units)
            label.adjustSize()

    def value(self):
        """Return the current value of the slider"""
        return 0


if __name__ == '__main__':
    app = QApplication([])

    slider = SliderDisplay('Magnitude', 0, 10, units='dB')

    slider.show()

    app.exec_()
