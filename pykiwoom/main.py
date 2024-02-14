from PyQt5 import QtWidgets, uic
from ui import Ui_MainWindow
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = Ui_MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()