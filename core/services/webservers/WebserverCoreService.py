from core.repository import WebserverRepository
from core.database.model.webserver import WebserverSetting

class WebserverCoreService(WebserverRepository):
    def __init__(self):
        pass

# noinspection PyUnresolvedReferences
def load_settings(self,server_name: str) -> WebserverSetting | None:
    print(f"SERVICE: Đang tải cấu hình cho {server_name}...")
    return WebserverRepository.get_webserver_settings(server_name)


def save_settings(self,settings_data: dict) -> bool:
    """
    Nhận dữ liệu thô (dict) từ lớp UI, chuyển đổi và lưu lại.
    Đây là nơi chứa logic nghiệp vụ.
    """
    try:
        # Business Logic 1: Chuyển đổi dict thành Model object
        setting_model = WebserverSetting(**settings_data)

        # Business Logic 2: (Ví dụ) Kiểm tra dữ liệu
        if setting_model.http_port == setting_model.ssl_port:
            raise ValueError("Cổng HTTP và SSL không được trùng nhau.")

        # Gọi xuống lớp CRUD để thực hiện lưu trữ
        success = WebserverRepository.update_webserver_settings(setting_model)

        # Business Logic 3: (Ví dụ) Ghi log
        if success:
            print(f"SERVICE: Đã lưu thành công cho {setting_model.server_name}.")

        return success
    except Exception as e:
        print(f"SERVICE ERROR: {e}")
        return False

def load_webservers_versions(self)
