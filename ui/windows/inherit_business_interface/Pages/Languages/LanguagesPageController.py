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

        # Chạy các hàm khởi tạo hoặc lấy dữ liệu ban đầu
        try:
            # Phiên bản cho hộp combobox
            languages_version_data = self.language_core_service.load_languages_version()
            if languages_version_data is None:
                QMessageBox.warning(self, "Cảnh báo", "Dữ liệu trong database đang rỗng!")
            else:
                for key, row in languages_version_data.items():
                    combobox = getattr(self.ui,f"{key}_combobox")
                    combobox.addItems([sqlite_row["version"] for sqlite_row in row])
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Database versions có lỗi {str(e)}")
        try:
            # Cấu hình ngôn ngữ đang được chọn
            languages_init_data = self.language_core_service.load_data()
            print(languages_init_data)
            if languages_init_data is None:
                QMessageBox.warning(self,"Cảnh báo","Dữ liệu trong database đang rỗng!")
            else:
                chosen_language = None
                for language_setting in languages_init_data:
                    self.init_settings_data(language_setting.language, language_setting)
                    if language_setting.is_chosen:
                        chosen_language = language_setting.language

                if chosen_language:
                    radio_button = getattr(self.ui, f"{chosen_language}_radio")
                    radio_button.setChecked(True)
                    self.on_language_selected(chosen_language)
                else: self.on_language_selected("")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Database settings có lỗi: {str(e)}")

        # Gán sự kiện cho các nút
        self.ui.language_save_change_buttonbox.clicked.connect(self.on_save_changes)
        self.ui.php_radio.clicked.connect(lambda checked: self.on_language_selected("php"))
        self.ui.python_radio.clicked.connect(lambda checked: self.on_language_selected("python"))
        self.ui.java_radio.clicked.connect(lambda checked: self.on_language_selected("java"))
        self.ui.nodejs_radio.clicked.connect(lambda checked: self.on_language_selected("nodejs"))

        for lang in self.LANGUAGE_GROUP.keys():
            try:
                ssl_checkbox = getattr(self.ui, f"{lang}_ssl_enabled_checkbox")
                ssl_checkbox.toggled.connect(
                    lambda checked, l=lang: self._set_ssl_checkbox_toggled(l, checked)
                )
            except AttributeError as e:
                print(f"Lỗi: Không tìm thấy {lang}_ssl_enabled_checkbox: {e}")

    def on_save_changes(self):
        print("Lưu cấu hình languages...")

    def init_settings_data(self, language, data):
        try:
            combobox_widget = getattr(self.ui, f"{language}_combobox")
            combobox_widget.setCurrentText(data.selected_version)
            lineedit_widget = getattr(self.ui, f"{language}_root_folder_lineedit")
            lineedit_widget.setText(data.root_folder if data.root_folder is not None else "")
            checkbox_widget = getattr(self.ui, f"{language}_ssl_enabled_checkbox")
            checkbox_widget.setChecked(data.is_ssl_enabled)

        except AttributeError as e:
            QMessageBox.critical(self, "Lỗi Giao diện", f"Không tìm thấy widget cho ngôn ngữ '{language}': {e}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi khởi tạo dữ liệu cho {language}: {e}")


    def on_language_selected(self, language):
        for str_language, widgets in LanguagesPageController.LANGUAGE_GROUP.items():
            enabled = str_language == language
            for str_widget in widgets:
                widget = getattr(self.ui, str_widget)
                widget.setEnabled(enabled)

            if enabled:
                try:
                    ssl_checkbox = getattr(self.ui, f"{str_language}_ssl_enabled_checkbox")
                    port_lineedit = getattr(self.ui, f"{str_language}_port_lineedit")
                    port_lineedit.setEnabled(ssl_checkbox.isChecked())
                except AttributeError:
                    pass
                else:
                    try:
                        port_lineedit = getattr(self.ui, f"{str_language}_port_lineedit")
                        port_lineedit.setEnabled(False)
                    except AttributeError:
                        pass

    def _set_ssl_checkbox_toggled(self,language,enabled):
        try:
            port_lineedit = getattr(self.ui, f"{language}_port_lineedit")
            port_lineedit.setEnabled(enabled)
        except AttributeError as e:
            print(f"Lỗi: Không tìm thấy widget cho {language}_port_lineedit: {e}")