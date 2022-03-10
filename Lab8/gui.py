#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout


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

        # A button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # You probably want to add in other interface elements here

        # Add things to the layout
        layout.addWidget(quit_button)

        # Add other widgets to the layout here.  Possibly other layouts.


if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()

