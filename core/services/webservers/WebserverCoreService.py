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
            model_data = {
                'server_name': settings_data.get('type'),
                'selected_version': settings_data.get('version'),
                'executable_path': settings_data.get('executable_path'),
                'sites_enabled_path': settings_data.get('sites_enabled_path'),
                'tld_template': settings_data.get('tld'),
                'http_port': settings_data.get('listen_port'),
                'ssl_port': None,
                'alp_path': settings_data.get('access_log_path'),
                'elp_path': settings_data.get('error_log_path'),
                'is_enabled': True
            }
            setting_model = WebserverSetting(**settings_data)

            success = self.__class__.webserver_repository.update_webserver_settings(setting_model)

            if success:
                print(f"SERVICE: Đã lưu thành công cho {setting_model.server_name}.")

            return success
        except Exception as e:
            print(f"SERVICE ERROR: {e}")
            return False

    def load_webservers_versions(self):
        return self.__class__.webserver_repository.get_all_webserver_versions()