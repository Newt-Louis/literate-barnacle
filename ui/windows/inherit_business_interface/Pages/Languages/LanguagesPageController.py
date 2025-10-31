from PySide6.QtWidgets import QWidget
from ui.windows.origin_interface import Ui_LanguagesPage
from .LanguagesServiceController import LanguagesServiceController


class LanguagesPageController(QWidget):
    BROWSE_MAP = {}
    WIDGET_MAP = {
        "php": [
            "self.ui.php_combobox",
            "self.ui.php_ssl_enabled_checkbox",
            "self.ui.php_port_lineedit",
            "self.ui.php_root_folder_lineedit",
            "self.ui.php_browse_root_folder_pushbutton",
        ],
        "python": [
            "self.ui.python_combobox",
            "self.ui.python_ssl_enabled_checkbox",
            "self.ui.python_port_lineedit",
            "self.ui.python_root_folder_lineedit",
            "self.ui.python_browse_root_folder_pushbutton",
        ],
        "java": [
            "self.ui.java_combobox",
            "self.ui.java_ssl_enabled_checkbox",
            "self.ui.java_port_lineedit",
            "self.ui.java_root_folder_lineedit",
            "self.ui.java_browse_root_folder_pushbutton",
        ],
        "nodejs": [
            "self.ui.nodejs_combobox",
            "self.ui.nodejs_ssl_enabled_checkbox",
            "self.ui.nodejs_port_lineedit",
            "self.ui.nodejs_root_folder_lineedit",
            "self.ui.nodejs_browse_root_folder_pushbutton",
        ],
    }
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.ui = Ui_LanguagesPage()
        self.ui.setupUi(self)
        self.language_core_service = LanguagesServiceController()

        # Gán sự kiện cho các nút
        self.ui.language_save_change_buttonbox.clicked.connect(self.on_save_changes)
        self.ui.php_radio.toggled.connect(lambda checked: self.on_language_selected("php"))

        # Chạy các hàm khởi tạo hoặc lấy dữ liệu ban đầu
        languages_init_data = self.language_core_service.load_data()
        print("Dữ liệu ban đầu hoặc đã được lưu trữ",languages_init_data)

    def on_save_changes(self):
        print("Lưu cấu hình languages...")

    def on_language_selected(self, language):
        print("PHP được chọn.")