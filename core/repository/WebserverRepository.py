import sqlite3, os
from core.config import config
from core.database.model.webserver.WebserverSetting import WebserverSetting

DB_PATH = config.DB_PATH
# noinspection PyUnresolvedReferences
def get_all_webserver_settings() -> list[WebserverSetting] | None:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM webserver_settings")
            rows = cursor.fetchall()

            if rows:
                return [WebserverSetting(**dict(row)) for row in rows]
            return None
    except sqlite3.Error as e:
        print(f"Lỗi database khi lấy cài đặt {server_name}: {e}")
        raise


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

def get_all_webserver_versions() -> dict[str, list[sqlite3.Row]]:
    versions_dict = {
        "apache": [],
        "nginx": []
    }
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(""" SELECT * FROM webserver_versions """)
            rows = cursor.fetchall()

            for row in rows:
                # sử dụng sqlite3.Row để gọi được tên cột
                server_type = row["type"]

                # Kiểm tra xem type có hợp lệ không và thêm vào danh sách tương ứng
                if server_type in versions_dict:
                    versions_dict[server_type].append(row)

            return versions_dict
    except sqlite3.Error as e:
        print(f"Lỗi database khi lấy danh sách phiên bản: {e}")
        return {"apache": [], "nginx": []}

def sync_versions_to_db(server_type: str, directory_path: str):
    print(f"Bắt đầu đồng bộ hóa phiên bản cho '{server_type}' từ: {directory_path}")

    # Bước 1: Quét thư mục để lấy danh sách các phiên bản hiện tại
    try:
        versions = {
            name for name in os.listdir(directory_path)
            if os.path.isdir(os.path.join(directory_path, name))
        }
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy thư mục: {directory_path}")
        return

    # Bước 2: Mở kết nối và thực hiện các thay đổi trong một transaction
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            # Kiểm tra đồng bộ dữ liệu
            cursor.execute("SELECT version FROM webserver_versions WHERE type = ?", (server_type,))
            versions_in_db = {row[0] for row in cursor.fetchall()}
            if versions == versions_in_db:
                print("✅ Dữ liệu đã đồng bộ. Không cần cập nhật.")
                return

    # Bước 3: Xóa TẤT CẢ các dòng có type tương ứng
            print(f"Phát hiện các phiên bản có thay đổi: {versions}")
            print(f"Đang xóa các phiên bản '{server_type}' cũ khỏi database...")
            cursor.execute("DELETE FROM webserver_versions WHERE type = ?", (server_type,))

    # Bước 4: Chèn lại danh sách phiên bản mới
            if versions:
                print(f"Đang chèn các phiên bản mới vào database...")
                # Chuẩn bị dữ liệu dưới dạng list of tuples
                data_to_insert = [(server_type, version) for version in versions]
                # Dùng executemany để chèn nhiều dòng cùng lúc
                cursor.executemany(
                    "INSERT INTO webserver_versions (type, version) VALUES (?, ?)",
                    data_to_insert
                )

            # conn.commit() được tự động gọi khi khối 'with' kết thúc thành công
            print(f"Đồng bộ hóa cho '{server_type}' hoàn tất.")
    except sqlite3.Error as e:
        print(f"LỖI DATABASE khi đồng bộ hóa: {e}")

def disable_all_webservers() -> bool:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE webserver_settings SET is_enabled = 0")
            conn.commit()
            return True
    except sqlite3.Error as e:
        return False