from PySide6.QtWidgets import QWidget
from ui.windows.origin_interface import Ui_WebserverPage


class WebserverPageController(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model

        self.ui = Ui_WebserverPage()

        self.ui.setupUi(self)

        self.ui.apache_radio.setChecked(True)
        self.ui.apache_radio.toggled.connect(self.on_webserver_changed)
        self.ui.nginx_radio.toggled.connect(self.on_webserver_changed)
        self.ui.webserver_save_change_buttonbox.clicked.connect(self.on_save_changes)

        # Gọi cập nhật thay đổi cho lần đầu tiên
        self.on_webserver_changed()

    def on_save_changes(self):
        print("Lưu cấu hình apache...")

    def on_apache_selected(self, checked):
        if checked:
            print("Apache được chọn.")

    def on_webserver_changed(self):
        if self.ui.apache_radio.isChecked():
            print("Apache đang được chọn")
            self.ui.nginx_select_version_combobox.setVisible(False)
            self.ui.nginx_excutable_lineEdit.setVisible(False)
            self.ui.nginx_excutable_browseButton.setVisible(False)
            self.ui.nginx_sites_enabled_lineEdit.setVisible(False)
            self.ui.nginx_sites_enabled_browseButton.setVisible(False)
            self.ui.nginx_listen_port_lineEdit.setVisible(False)
            self.ui.nginx_config_tld_lineEdit.setVisible(False)
            self.ui.nginx_alp_lineEdit.setVisible(False)
            self.ui.nginx_alp_browseButton.setVisible(False)
            self.ui.nginx_elp_lineEdit.setVisible(False)
            self.ui.nginx_elp_browseButton.setVisible(False)
            self.ui.apache_select_version_combobox.setVisible(True)
            self.ui.apache_excutable_lineEdit.setVisible(True)
            self.ui.apache_excutable_browseButton.setVisible(True)
            self.ui.apache_sites_enabled_lineEdit.setVisible(True)
            self.ui.apache_sites_enabled_browseButton.setVisible(True)
            self.ui.apache_listen_port_lineEdit.setVisible(True)
            self.ui.apache_config_tld_lineEdit.setVisible(True)
            self.ui.apache_alp_lineEdit.setVisible(True)
            self.ui.apache_alp_browseButton.setVisible(True)
            self.ui.apache_elp_lineEdit.setVisible(True)
            self.ui.apache_elp_browseButton.setVisible(True)
        elif self.ui.nginx_radio.isChecked():
            print("Nginx đang được chọn")
            self.ui.nginx_select_version_combobox.setVisible(True)
            self.ui.nginx_excutable_lineEdit.setVisible(True)
            self.ui.nginx_excutable_browseButton.setVisible(True)
            self.ui.nginx_sites_enabled_lineEdit.setVisible(True)
            self.ui.nginx_sites_enabled_browseButton.setVisible(True)
            self.ui.nginx_listen_port_lineEdit.setVisible(True)
            self.ui.nginx_config_tld_lineEdit.setVisible(True)
            self.ui.nginx_alp_lineEdit.setVisible(True)
            self.ui.nginx_alp_browseButton.setVisible(True)
            self.ui.nginx_elp_lineEdit.setVisible(True)
            self.ui.nginx_elp_browseButton.setVisible(True)
            self.ui.apache_select_version_combobox.setVisible(False)
            self.ui.apache_excutable_lineEdit.setVisible(False)
            self.ui.apache_excutable_browseButton.setVisible(False)
            self.ui.apache_sites_enabled_lineEdit.setVisible(False)
            self.ui.apache_sites_enabled_browseButton.setVisible(False)
            self.ui.apache_listen_port_lineEdit.setVisible(False)
            self.ui.apache_config_tld_lineEdit.setVisible(False)
            self.ui.apache_alp_lineEdit.setVisible(False)
            self.ui.apache_alp_browseButton.setVisible(False)
            self.ui.apache_elp_lineEdit.setVisible(False)
            self.ui.apache_elp_browseButton.setVisible(False)