from PySide6.QtWidgets import QWidget
from ui.windows.origin_interface import Ui_DashboardPage
from core.manager.EventBus import EventBus


class DashboardPageController(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.ui = Ui_DashboardPage()
        self.ui.setupUi(self)

        self.ui.startall_button.clicked.connect(self.on_save_changes)
        EventBus.webserver_saved.connect(self.listener_webserver_saved)

    def on_save_changes(self):
        print("Lưu cấu hình databases...")
        # Lấy dữ liệu từ self.ui.mysql_version_combobox.currentText()
        # và gọi self.model.save_config(...)

    def on_mysql_selected(self, checked):
        if checked:
            print("MySQL được chọn.")

    def listener_webserver_saved(self,data):
        print("đã nhận được dữ liệu sau khi lưu từ webserver",data)
        self.ui.webserver_type_label.setText(data["server_name"])
        self.ui.webserver_version_label.setText(data["selected_version"])
