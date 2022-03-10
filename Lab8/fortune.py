#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel

class FortuneTeller(QMainWindow):
    def __init__(self):
        super(FortuneTeller, self).__init__()

        self.setWindowTitle('Fortune teller')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)

        # A layout - in this case, a vertical one
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Create a label (non-editable text) and add it to the vertical layout
        self.title_label = QLabel('All-Knowing Fortune Teller')
        layout.addWidget(self.title_label)

        # Add a button and add it to the vertical layout
        self.button = QPushButton('Give Fortune')
        layout.addWidget(self.button)

        # Add a second label
        self.fortune_label = QLabel()
        layout.addWidget(self.fortune_label)


if __name__ == '__main__':
    app = QApplication([])
    interface = FortuneTeller()
    interface.show()
    app.exec_()