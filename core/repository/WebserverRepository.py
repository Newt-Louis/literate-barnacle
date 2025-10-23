import sqlite3
from core.config import config
from core.database.model.webserver import WebserverSetting

# noinspection PyUnresolvedReferences
def get_webserver_settings(server_name: str) -> WebserverSetting | None:
    """Lấy cài đặt cho một web server và trả về một đối tượng WebserverSetting."""
    try:
        with sqlite3.connect(config.DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM webserver_settings WHERE server_name = ?", (server_name,))
            row = cursor.fetchone()

            if row:
                return WebserverSetting(**dict(row))
            return None
    except sqlite3.Error as e:
        print(f"Lỗi database khi lấy cài đặt {server_name}: {e}")
        return None


def update_webserver_settings(setting: WebserverSetting):
    try:
        with sqlite3.connect(config.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           UPDATE webserver_settings
                           SET selected_version   = ?,
                               executable_path    = ?,
                               sites_enabled_path = ?,
                               tld_template       = ?,
                               http_port          = ?,
                               ssl_port           = ?
                           WHERE server_name = ?
                           """, (
                               setting.selected_version,
                               setting.executable_path,
                               setting.sites_enabled_path,
                               setting.tld_template,
                               setting.http_port,
                               setting.ssl_port,
                               setting.server_name
                           ))
            conn.commit()
            print(f"Đã cập nhật thành công cho {setting.server_name}")
            return True
    except sqlite3.Error as e:
        print(f"Lỗi database khi cập nhật {setting.server_name}: {e}")
        return False