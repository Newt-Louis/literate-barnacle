from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QRadioButton, QFileDialog, QMessageBox
from ui.windows.origin_interface import Ui_LanguagesPage
from .LanguagesServiceController import LanguagesServiceController


class LanguagesPageController(QWidget):
    BROWSE_MAP = {
        "php_browse_root_folder_pushbutton":("file","php_root_folder_lineedit","(*.exe)"),
        "python_browse_root_folder_pushbutton":("file","python_root_folder_lineedit","(*.exe)"),
        "java_browse_root_folder_pushbutton":("file","java_root_folder_lineedit","(*.exe)"),
        "nodejs_browse_root_folder_pushbutton":("file","nodejs_root_folder_lineedit","(*.exe)"),
    }
    LANGUAGE_GROUP = {
        "php": [
            "php_combobox",
            "php_ssl_enabled_checkbox",
            "php_port_lineedit",
            "php_root_folder_lineedit",
            "php_browse_root_folder_pushbutton",
        ],
        "python": [
            "python_combobox",
            "python_ssl_enabled_checkbox",
            "python_port_lineedit",
            "python_root_folder_lineedit",
            "python_browse_root_folder_pushbutton",
        ],
        "java": [
            "java_combobox",
            "java_ssl_enabled_checkbox",
            "java_port_lineedit",
            "java_root_folder_lineedit",
            "java_browse_root_folder_pushbutton",
        ],
        "nodejs": [
            "nodejs_combobox",
            "nodejs_ssl_enabled_checkbox",
            "nodejs_port_lineedit",
            "nodejs_root_folder_lineedit",
            "nodejs_browse_root_folder_pushbutton",
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
        self.ui.php_radio.clicked.connect(lambda checked: self.on_language_selected("php", checked))
        self.ui.python_radio.clicked.connect(lambda checked: self.on_language_selected("python", checked))
        self.ui.java_radio.clicked.connect(lambda checked: self.on_language_selected("java", checked))
        self.ui.nodejs_radio.clicked.connect(lambda checked: self.on_language_selected("nodejs", checked))

        # Chạy các hàm khởi tạo hoặc lấy dữ liệu ban đầu
        languages_init_data = self.language_core_service.load_data()
        print("Dữ liệu ban đầu hoặc đã được lưu trữ",languages_init_data)

    def on_save_changes(self):
        print("Lưu cấu hình languages...")

    def on_language_selected(self, language, checked):
        for str_language, widgets in LanguagesPageController.LANGUAGE_GROUP.items():
            enabled = str_language == language
            for str_widget in widgets:
                widget = getattr(self.ui, str_widget)
                widget.setEnabled(enabled)

    def _set_group_enabled(self,language,enabled):
        widgets = LanguagesPageController.LANGUAGE_GROUP[language]
        for str_widget in widgets:
            widget = getattr(self.ui, str_widget)
            if isinstance(widget, QtWidgets.QRadioButton):
                continue
            widget.setEnabled(enabled)