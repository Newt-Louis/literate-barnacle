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
        print("Chạy tất cả dịch vụ ...")

        self.ui.startall_button.setText("Stop")

    def start_database(self, checked):
        # TODO: chạy dịch vụ database
        if checked:
            print("Database đang chạy...")

    def start_webserver(self):
        print("Webserver đang chạy...")

    def start_tools(self):
        print("Tool redis hoặc memcached hoặc terminal độc lập của ứng dụng đang chạy")

    def start_language(self):
        print("Ngôn ngữ được chọn hoặc thư mục gốc của ngôn ngữ được thay đổi")

    def start_network(self):
        print("Chạy độc lập loại network nào đó ví dụ ngrok hoặc telnet")

    def listener_webserver_saved(self,data):
        print("đã nhận được dữ liệu sau khi lưu từ webserver",data)
        self.ui.webserver_type_label.setText(data["server_name"])
        self.ui.webserver_version_label.setText(data["selected_version"])

        print("cập nhật thông tin webserver thành công") if self.dashboard_service.update_webserver_info(data) else print("có lỗi khi cập nhật với sqlite")

    def listener_database_saved(self,data):
        print("nhận emit từ database rồi lưu thông tin")

    def listener_language_saved(self,data):
        print("nhận emit từ language rồi lưu thông tin")

    def listener_network_saved(self,data):
        print("nhận emit từ network rồi lưu thông tin")

    def listener_tool_saved(self,data):
        print("nhận emit từ tool rồi lưu thông tin")