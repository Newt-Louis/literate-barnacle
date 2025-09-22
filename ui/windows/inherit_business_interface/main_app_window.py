# ui/windows/main_app_window.py

from PySide6.QtWidgets import QMainWindow
# Import class giao diện đã được tạo tự động
from ui.windows.origin_interface import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        # Gọi hàm khởi tạo của lớp cha (QMainWindow)
        super().__init__()

        # Tạo một đối tượng từ class giao diện
        self.ui = Ui_MainWindow()
        # Dùng phương thức setupUi để vẽ giao diện lên cửa sổ chính (self)
        self.ui.setupUi(self)

        # Đặt tiêu đề cho cửa sổ
        # self.setWindowTitle("Local WebServer Stacks Manager")

        # Gọi phương thức để kết nối các tín hiệu (signals) và hành động (slots)
        self._connect_signals()

        # Thiết lập trang mặc định khi mở ứng dụng
        self.ui.dashboard_button.setChecked(True)  # Đánh dấu nút Dashboard là đang được chọn
        self.ui.main_content_area.setCurrentWidget(self.ui.dashboard_page)

    def _connect_signals(self):
        """
        Nơi tập trung kết nối tất cả các tín hiệu từ widgets.
        """
        # Kết nối các nút bấm ở sidebar với phương thức chuyển trang
        self.ui.dashboard_button.clicked.connect(
            lambda: self.ui.main_content_area.setCurrentWidget(self.ui.dashboard_page))
        self.ui.languages_button.clicked.connect(
            lambda: self.ui.main_content_area.setCurrentWidget(self.ui.languages_page))
        self.ui.databases_button.clicked.connect(
            lambda: self.ui.main_content_area.setCurrentWidget(self.ui.databases_page))
        self.ui.webserver_button.clicked.connect(
            lambda: self.ui.main_content_area.setCurrentWidget(self.ui.webserver_page))
        self.ui.tools_button.clicked.connect(lambda: self.ui.main_content_area.setCurrentWidget(self.ui.tools_page))
        self.ui.network_button.clicked.connect(lambda: self.ui.main_content_area.setCurrentWidget(self.ui.network_page))