from PySide6.QtWidgets import QWidget, QRadioButton, QFileDialog
from ui.windows.origin_interface import Ui_WebserverPage


class WebserverPageController(QWidget):
    BROWSE_MAP = {
        "apache_excutable_browseButton": ("file","apache_excutable_lineEdit","(*.exe)"),
        "apache_sites_enabled_browseButton": ("folder","apache_sites_enabled_lineEdit",""),
        "apache_alp_browseButton": ("folder","apache_alp_lineEdit",""),
        "apache_elp_browseButton": ("folder","apache_elp_lineEdit",""),
        "nginx_excutable_browseButton": ("file", "nginx_excutable_lineEdit", "(*.exe)"),
        "nginx_sites_enabled_browseButton": ("folder", "nginx_sites_enabled_lineEdit", ""),
        "nginx_alp_browseButton": ("folder", "nginx_alp_lineEdit", ""),
        "nginx_elp_browseButton": ("folder", "nginx_elp_lineEdit", ""),
    }
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.ui = Ui_WebserverPage()
        self.ui.setupUi(self)

        # Gắn sự kiện
        self.ui.apache_radio.clicked.connect(self.on_webserver_changed)
        self.ui.nginx_radio.clicked.connect(self.on_webserver_changed)
        self.ui.webserver_save_change_buttonbox.clicked.connect(self.on_save_changes)
        for button in self.findChildren(QWidget):
            name = button.objectName()
            #Gắn sự kiện cho tất cả nút Browse
            if name.endswith("_browseButton"):
                button.clicked.connect(self.on_browse_button_clicked)

        # Set mặc định chọn radio apache đầu tiên
        self.ui.apache_radio.setChecked(True)
        # Gọi cập nhật thay đổi disabled cho lần đầu tiên
        self.on_webserver_changed()

    def on_save_changes(self):
        print("Lưu cấu hình apache...")

    def on_apache_selected(self, checked):
        if checked:
            print("Apache được chọn.")

    def set_group_enabled(self, prefix, enabled):
        for widget in self.findChildren(QWidget):
            if widget.objectName().startswith(prefix):
                if isinstance(widget,QRadioButton):
                    continue
                else:
                    widget.setEnabled(enabled)

    def on_webserver_changed(self):
        if self.ui.apache_radio.isChecked():
            self.set_group_enabled("apache_", True)
            self.set_group_enabled("nginx_", False)
        elif self.ui.nginx_radio.isChecked():
            self.set_group_enabled("apache_", False)
            self.set_group_enabled("nginx_", True)

    def on_browse_button_clicked(self):
        """Xử lý khi click bất kỳ nút Browse nào"""
        sender = self.sender()
        name = sender.objectName()
        print(f"Clicked: {name}")
        if name not in self.__class__.BROWSE_MAP:
            return

        browse_type, lineedit_name, file_filter = self.__class__.BROWSE_MAP[name]
        line_edit = getattr(self.ui, lineedit_name)

        if browse_type == "file":
            file_path, _ = QFileDialog.getOpenFileName(self, "Chọn file", "", file_filter)
            if file_path:
                line_edit.setText(file_path)
        else:  # folder
            folder = QFileDialog.getExistingDirectory(self, "Chọn thư mục", "")
            if folder:
                line_edit.setText(folder)


    # Các widget hiện đang có trong WebserverPage
    # Apache:
    #         self.ui.apache_select_version_combobox
    #         self.ui.apache_excutable_lineEdit
    #         self.ui.apache_excutable_browseButton
    #         self.ui.apache_sites_enabled_lineEdit
    #         self.ui.apache_sites_enabled_browseButton
    #         self.ui.apache_listen_port_lineEdit
    #         self.ui.apache_config_tld_lineEdit
    #         self.ui.apache_alp_lineEdit
    #         self.ui.apache_alp_browseButton
    #         self.ui.apache_elp_lineEdit
    #         self.ui.apache_elp_browseButton
    # Nginx
    #         self.ui.nginx_select_version_combobox
    #         self.ui.nginx_excutable_lineEdit
    #         self.ui.nginx_excutable_browseButton
    #         self.ui.nginx_sites_enabled_lineEdit
    #         self.ui.nginx_sites_enabled_browseButton
    #         self.ui.nginx_listen_port_lineEdit
    #         self.ui.nginx_config_tld_lineEdit
    #         self.ui.nginx_alp_lineEdit
    #         self.ui.nginx_alp_browseButton
    #         self.ui.nginx_elp_lineEdit
    #         self.ui.nginx_elp_browseButton