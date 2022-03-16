from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QSlider, QLineEdit, QFileDialog
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import digital_signal as ds

class GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('GUI')
    # Textbox
        self.start_text = QLineEdit(self)
        self.end_text = QLineEdit(self)
        self.load_text = QLineEdit(self)
        self.save_text = QLineEdit(self)
    # Load GUI
        self.setWindowTitle('Yes')
        self.setGeometry(10, 10, 640, 480)
    # Slider
    #     self.low = 0
    #     self.high = 100
        self.sl_low = QSlider(Qt.Horizontal)
        self.sl_high = QSlider(Qt.Horizontal)
    # Label
        lab_low = QLabel('Low: ', self)
        self.sl_low.valueChanged.connect(lambda: low_slide())
        lab_high = QLabel('High: ', self)
        self.sl_high.valueChanged.connect(lambda: high_slide())
        lab_start = QLabel('Start: ', self)
        lab_end = QLabel('End: ', self)
        lab_load = QLabel('Load file: ', self)
        lab_save = QLabel('Save file: ', self)
    # Button
        reset_button = QPushButton('Reset all')
        reset_button.clicked.connect(self.reset_all)
        load_button = QPushButton('Load')
        load_button.clicked.connect(self.load_wav)
        save_button = QPushButton('Save')
        save_button.clicked.connect(self.save_wav)
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
        left_layout.addWidget(self.sl_low)
        left_layout.addWidget(lab_high)
        left_layout.addWidget(self.sl_high)
        right_layout.addWidget(lab_start)
        right_layout.addWidget(self.start_text)
        right_layout.addWidget(lab_end)
        right_layout.addWidget(self.end_text)
        right_layout.addWidget(reset_button)
        left_layout.addWidget(lab_load)
        left_layout.addWidget(self.load_text)
        left_layout.addWidget(load_button)
        left_layout.addWidget(lab_save)
        left_layout.addWidget(self.save_text)
        left_layout.addWidget(save_button)

        def low_slide():
            value = self.sl_low.value()
            lab_low.setText("Low: " + "%.3f" % value + " Hz")
            lab_low.adjustSize()
            self.low = self.sl_low.value()

        def high_slide():
            value = self.sl_high.value()
            lab_high.setText("High: " + "%.3f" % value + " Hz")
            lab_high.adjustSize()
            self.high = self.sl_high.value()

    def load_wav(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        signal = ds.DigitalSignal.from_wav(fileName)
        length = signal.source_data.shape[0] / signal.sampling_frequency
        time = np.linspace(0., length, signal.source_data.shape[0])
        # Set Range of slider
        self.sl_low.setRange(0, int(signal.freq_high))
        self.sl_high.setRange(0, int(signal.freq_high))
        # Set text of Qline
        self.start_text.setText('0')
        self.end_text.setText((str(round(time[-1], 2))))

        # Plotting
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(time, signal.source_data[:])
        ax.set_title(fileName)
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Amplitude')
        self.display.draw()
        self.load_text.setText(fileName)

    def save_wav(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        self.save_text.setText(fileName)

    def reset_all(self):
        self.sl_low.setValue(0)
        self.sl_high.setValue(0)
        self.start_text.setText('0')
        self.end_text.setText('0')


if __name__ == '__main__':
    app = QApplication([])
    gui = GUI()
    gui.show()
    app.exec_()
