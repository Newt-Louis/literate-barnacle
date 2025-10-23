from core.repository import WebserverRepository
from core.database.model.webserver.WebserverSetting import WebserverSetting

class WebserverCoreService:
    webserver_repository = WebserverRepository

    def __init__(self):
        pass

    # noinspection PyUnresolvedReferences
    def load_settings(self, server_name: str) -> WebserverSetting | None:
        print(f"SERVICE: Đang tải cấu hình cho {server_name}...")
        return self.__class__.webserver_repository.get_webserver_settings(server_name)


    def save_settings(self, settings_data: dict) -> bool:
        try:
            # Business Logic 1: Chuyển đổi dict thành Model object
            setting_model = WebserverSetting(**settings_data)

            # Business Logic 2: (Ví dụ) Kiểm tra dữ liệu
            if setting_model.http_port == setting_model.ssl_port:
                raise ValueError("Cổng HTTP và SSL không được trùng nhau.")

            # Gọi xuống lớp CRUD để thực hiện lưu trữ
            success = self.__class__.webserver_repository.update_webserver_settings(setting_model)

            # Business Logic 3: (Ví dụ) Ghi log
            if success:
                print(f"SERVICE: Đã lưu thành công cho {setting_model.server_name}.")

            return success
        except Exception as e:
            print(f"SERVICE ERROR: {e}")
            return False

    def load_webservers_versions(self):
        return self.__class__.webserver_repository.get_all_webserver_versions()