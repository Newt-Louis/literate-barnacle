from PySide6.QtWidgets import QWidget
# 1. Import lớp giao diện đã được build từ file .py
from ui.windows.origin_interface import Ui_ToolsPage


class ToolsPageController(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model

        # 2. Khởi tạo một đối tượng từ lớp giao diện
        self.ui = Ui_ToolsPage()

        # 3. Dùng phương thức setupUi() để vẽ giao diện lên chính widget controller này (self)
        self.ui.setupUi(self)

    def on_save_changes(self):
        print("Lưu cấu hình redis...")

    def on_redis_selected(self, checked):
        if checked:
            print("Redis đang được bật.")
