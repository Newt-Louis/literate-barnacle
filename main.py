import sys
from PySide6 import QtWidgets
from ui.windows.inherit_business_interface.MainAppWindow import MainAppWindow
from core.database.database_setup import run_migrations
from core.services.SynchronizationService import run_all_startup_syncs
from core.manager.DirectoryWatcher import start_watching
from core.manager.DashboardManagement import DashboardManagement

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainAppWindow()
    run_migrations()
    run_all_startup_syncs()
    print("Đồng bộ hóa hoàn tất.")
    start_watching()
    dashboard_session = DashboardManagement()
    dashboard_session.set("services_status",{
        "database": 0,
        "webserver": 0,
    })
    window.show()
    sys.exit(app.exec())