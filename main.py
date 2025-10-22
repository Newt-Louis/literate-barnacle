import sys
from PySide6 import QtWidgets
from ui.windows.inherit_business_interface.MainAppWindow import MainAppWindow
from core.database.database_setup import run_migrations

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainAppWindow()
    run_migrations()
    window.show()
    sys.exit(app.exec())