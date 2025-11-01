from PySide6.QtWidgets import QWidget

from .DashboardServiceController import DashboardServiceController
from ui.windows.origin_interface import Ui_DashboardPage
from core.manager.EventBus import EventBus
from core.manager.DashboardSession import DashboardSession


class DashboardPageController(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.ui = Ui_DashboardPage()
        self.ui.setupUi(self)
        self.dashboard_service = DashboardServiceController()
        self.dashboard_session = DashboardSession()

        # Nghe sự kiện phát ra từ các trang dịch vụ khác
        EventBus.webserver_saved.connect(self.listener_webserver_saved)

        # Gán hàm xử lý sự kiện cho nút start all
        self.ui.startall_button.clicked.connect(self.on_save_changes)
        self.ui.webserver_start_pushButton.clicked.connect(self.start_webserver)
        self.ui.database_start_pushButton.clicked.connect(self.start_database)
        self.ui.language_start_pushButton.clicked.connect(self.start_language)
        self.ui.tool_2_start_pushButton.clicked.connect(self.start_tools)
        self.ui.tool_3_start_pushButton.clicked.connect(self.start_tools)
        self.ui.network_start_pushButton.clicked.connect(self.start_network)

    def on_save_changes(self):
        start_all_status = self.dashboard_session.get("start_all_services")
        if start_all_status == 0:
            self.dashboard_session.set("start_all_services", 1)
            self.ui.startall_button.setText("Stop")
        else:
            self.dashboard_session.set("start_all_services", 0)
            self.ui.startall_button.setText("Start All")

    def start_database(self):
        database_status = self.dashboard_session.get("services_status")
        if "database" in database_status:
            match database_status["database"]:
                case 0:
                    self.ui.database_start_pushButton.setText("Stop")
                    self.dashboard_session.add_to_current_key("services_status", "database", 1)
                case 1:
                    self.ui.database_start_pushButton.setText("Start")
                    self.dashboard_session.add_to_current_key("services_status", "database", 0)

    def start_webserver(self):
        webserver_status = self.dashboard_session.get("services_status")
        if "webserver" in webserver_status:
            match webserver_status["webserver"]:
                case 0:
                    self.ui.webserver_start_pushButton.setText("Stop")
                    self.dashboard_session.add_to_current_key("services_status", "webserver", 1)
                case 1:
                    self.ui.webserver_start_pushButton.setText("Start")
                    self.dashboard_session.add_to_current_key("services_status","webserver",0)

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