from PySide6.QtWidgets import QWidget, QRadioButton
from ui.windows.origin_interface import Ui_WebserverPage


class WebserverPageController(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model

        self.ui = Ui_WebserverPage()

        self.ui.setupUi(self)

        self.ui.apache_radio.setChecked(True)
        self.ui.apache_radio.clicked.connect(self.on_webserver_changed)
        self.ui.nginx_radio.clicked.connect(self.on_webserver_changed)
        self.ui.webserver_save_change_buttonbox.clicked.connect(self.on_save_changes)

        # Gọi cập nhật thay đổi cho lần đầu tiên
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
            print("Apache được chọn 2")
            self.set_group_enabled("apache_", True)
            self.set_group_enabled("nginx_", False)
        elif self.ui.nginx_radio.isChecked():
            print("Nginx được chọn 2")
            self.set_group_enabled("apache_", False)
            self.set_group_enabled("nginx_", True)


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