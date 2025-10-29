from PySide6.QtWidgets import QWidget

from .DashboardServiceController import DashboardServiceController
from ui.windows.origin_interface import Ui_DashboardPage
from core.manager.EventBus import EventBus


class DashboardPageController(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.ui = Ui_DashboardPage()
        self.ui.setupUi(self)
        self.dashboard_service = DashboardServiceController()

        # Nghe sự kiện phát ra từ các trang dịch vụ khác
        EventBus.webserver_saved.connect(self.listener_webserver_saved)

        # Gán hàm xử lý sự kiện cho nút start all
        self.ui.startall_button.clicked.connect(self.on_save_changes)

    def on_save_changes(self):
        print("Lưu cấu hình databases...")
        # TODO: bắt đầu chạy tất cả dịch vụ nền đã được thiết lập
        # Lấy dữ liệu từ self.ui.mysql_version_combobox.currentText()
        # và gọi self.model.save_config(...)

    def start_database(self, checked):
        # TODO: chạy dịch vụ database
        if checked:
            print("Database đang chạy...")

    def start_webserver(self):
        print("Webserver đang chạy...")

    def start_tools(self):
        print("Tool ... đang chạy")

    def start_language(self):
        print("Ngôn ngữ được chọn hoặc thư mục gốc của ngôn ngữ được thay đổi")

    def listener_webserver_saved(self,data):
        print("đã nhận được dữ liệu sau khi lưu từ webserver",data)
        self.ui.webserver_type_label.setText(data["server_name"])
        self.ui.webserver_version_label.setText(data["selected_version"])

        print("cập nhật thông tin webserver thành công") if self.dashboard_service.update_webserver_info(data) else print("có lỗi khi cập nhật với sqlite")