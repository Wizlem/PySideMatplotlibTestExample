from PySide import QtGui, QtCore  # Import the PySide module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import design  # This file holds our MainWindow and all design related things
import testmodal

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods

import matplotlib
matplotlib.use('Qt4Agg')
import numpy as np

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        self.figure = Figure(figsize=(320,240), dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        self.plothl.addWidget(self.canvas)
        # It sets up layout and widgets that are defined
        self.actionStart.triggered.connect(self.OpenModal)


    def InputChanged(self):
        self.axes.clear()
        try:
            freq = float(self.InputBox.text())
            x = np.linspace(0, 6.28, int(100*freq))
            y = np.sin(freq*x)
            self.axes.plot(x, y)
            self.axes.set_xlim((0, 6.28))
            self.axes.set_ylim((-1, 1))
            self.statusbar.showMessage('freq = %f' % freq, 1000)
        except ValueError:
            pass

        self.canvas.draw()

    def OpenModal(self):
        testDialog = QtGui.QDialog(self)
        testUi = testmodal.Ui_Dialog()
        testUi.setupUi(testDialog)
        testDialog.show()

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
