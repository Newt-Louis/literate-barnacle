from PySide6.QtWidgets import QMainWindow
from ui.windows.origin_interface import Ui_MainWindow
from ui.windows.inherit_business_interface import DatabasesPageController
from ui.windows.inherit_business_interface import DashboardPageController
from ui.windows.inherit_business_interface import LanguagesPageController

class MainAppWindow(QMainWindow):
    def __init__(self):
        # Gọi hàm khởi tạo của lớp cha (QMainWindow)
        super().__init__()
        # self.core_model = AppModel()
        # Tạo một đối tượng từ class giao diện
        self.ui = Ui_MainWindow()
        # Dùng phương thức setupUi để vẽ giao diện lên cửa sổ chính (self)
        self.ui.setupUi(self)

        # Đặt tiêu đề cho cửa sổ
        # self.setWindowTitle("Local WebServer Stacks Manager")

        # Gọi phương thức để kết nối các tín hiệu (signals) và hành động (slots)
        self._connect_signals()

        # Thiết lập trang mặc định khi mở ứng dụng
        self.ui.databases_button.setChecked(True)  # Đánh dấu nút Dashboard là đang được chọn
        # self.ui.main_content_area.setCurrentWidget(self.ui.dashboard_page)

        # Khởi tạo các controller
        self.databases_page = DatabasesPageController(None)
        self.dashboard_page = DashboardPageController(None)
        self.languages_page = LanguagesPageController(None)
        # self.languages_page = LanguagesPageController(self.core_model)

        # Thêm chúng vào stacked widget
        self.ui.main_content_area.addWidget(self.databases_page)
        self.ui.main_content_area.addWidget(self.dashboard_page)
        self.ui.main_content_area.addWidget(self.languages_page)

        # Kết nối các nút sidebar
        self.ui.databases_button.clicked.connect(lambda: self.ui.main_content_area.setCurrentWidget(self.databases_page))
        self.ui.dashboard_button.clicked.connect(lambda: self.ui.main_content_area.setCurrentWidget(self.dashboard_page))
        self.ui.languages_button.clicked.connect(lambda: self.ui.main_content_area.setCurrentWidget(self.languages_page))
        # ...

    def _connect_signals(self):
        """
        Nơi tập trung kết nối tất cả các tín hiệu từ widgets.
        """
        # Kết nối các nút bấm ở sidebar với phương thức chuyển trang
        self.ui.dashboard_button.clicked.connect(
            lambda: self.ui.main_content_area.setCurrentWidget(self.dashboard_page))
        self.ui.languages_button.clicked.connect(
            lambda: self.ui.main_content_area.setCurrentWidget(self.languages_page))
        self.ui.databases_button.clicked.connect(
            lambda: self.ui.main_content_area.setCurrentWidget(self.databases_page))
        # self.ui.webserver_button.clicked.connect(
        #     lambda: self.ui.main_content_area.setCurrentWidget(self.ui.webserver_page))
        # self.ui.tools_button.clicked.connect(lambda: self.ui.main_content_area.setCurrentWidget(self.ui.tools_page))
        # self.ui.network_button.clicked.connect(lambda: self.ui.main_content_area.setCurrentWidget(self.ui.network_page))