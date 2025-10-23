import sqlite3, os
from core.config import config
from core.database.model import WebserverSetting
from core.database.model import WebserverVersion

DB_PATH = config.DB_PATH
# noinspection PyUnresolvedReferences
def get_webserver_settings(server_name: str) -> WebserverSetting | None:
    """Lấy cài đặt cho một web server và trả về một đối tượng WebserverSetting."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
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
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           UPDATE webserver_settings
                           SET selected_version   = ?,
                               executable_path    = ?,
                               sites_enabled_path = ?,
                               tld_template       = ?,
                               http_port          = ?,
                               ssl_port           = ?,
                               alp_path           = ?,
                               elp_path           = ?,
                               is_enabled         = ?
                           WHERE server_name = ?
                           """, (
                               setting.selected_version,
                               setting.executable_path,
                               setting.sites_enabled_path,
                               setting.tld_template,
                               setting.http_port,
                               setting.ssl_port,
                               setting.alp_path,
                               setting.elp_path,
                               setting.is_enabled,
                               setting.server_name
                           ))
            conn.commit()
            print(f"Đã cập nhật thành công cho {setting.server_name}")
            return True
    except sqlite3.Error as e:
        print(f"Lỗi database khi cập nhật {setting.server_name}: {e}")
        return False

def sync_versions_to_db(server_type: str, directory_path: str):
    """
    Quét một thư mục, xóa các phiên bản cũ trong DB và cập nhật lại
    với danh sách các thư mục hiện có.

    Args:
        server_type (str): 'apache' hoặc 'nginx'.
        directory_path (str): Đường dẫn đến thư mục cần quét (ví dụ: .../bin/apache).
    """
    print(f"Bắt đầu đồng bộ hóa phiên bản cho '{server_type}' từ: {directory_path}")

    # Bước 1: Quét thư mục để lấy danh sách các phiên bản hiện tại
    try:
        # Lấy tất cả các mục trong thư mục và chỉ giữ lại những mục là thư mục con
        versions = [
            name for name in os.listdir(directory_path)
            if os.path.isdir(os.path.join(directory_path, name))
        ]
        print(f"Đã phát hiện các phiên bản: {versions}")
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy thư mục: {directory_path}")
        return

    # Bước 2: Mở kết nối và thực hiện các thay đổi trong một transaction
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # Bước 2a: Xóa TẤT CẢ các dòng có type tương ứng
            print(f"Đang xóa các phiên bản '{server_type}' cũ khỏi database...")
            cursor.execute("DELETE FROM webserver_versions WHERE type = ?", (server_type,))

            # Bước 2b: Chèn lại danh sách phiên bản mới
            if versions:
                print(f"Đang chèn các phiên bản mới vào database...")
                # Chuẩn bị dữ liệu dưới dạng list of tuples
                data_to_insert = [(server_type, version) for version in versions]
                # Dùng executemany để chèn nhiều dòng cùng lúc, rất hiệu quả
                cursor.executemany(
                    "INSERT INTO webserver_versions (type, version) VALUES (?, ?)",
                    data_to_insert
                )

            # conn.commit() được tự động gọi khi khối 'with' kết thúc thành công
            print(f"Đồng bộ hóa cho '{server_type}' hoàn tất.")
    except sqlite3.Error as e:
        print(f"LỖI DATABASE khi đồng bộ hóa: {e}")