from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
 
from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(220, 32),
                QtWidgets.qApp.desktop().availableGeometry()
        ))
 
        self.acceptDrops()
        # set the title
        self.setWindowTitle("Image")
 
        # setting  the geometry of window
        self.setGeometry(0, 0, 1920, 1080)

        self.setWindowOpacity(0.5)
 
        # creating label
        self.label = QLabel(self)
         
        # loading image
        self.pixmap = QPixmap('resources/bigolof.png')
 
        # adding image to label
        self.label.setPixmap(self.pixmap)
 
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
 
        # show all the widgets
        self.show()

    def mousePressEvent(self, event):
        QtWidgets.qApp.quit()
    
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())