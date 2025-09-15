import sys
from PySide6 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.show()
    sys.exit(app.exec_())