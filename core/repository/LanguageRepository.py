import sqlite3, os
from core.config import config
from core.database.model.languages.LanguageSetting import LanguageSetting

DB_PATH = config.DB_PATH

def get_all_language_versions() -> dict[str, list[sqlite3.Row]]:
    versions_dict = {}
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(""" SELECT * FROM language_versions """)
            rows = cursor.fetchall()

            for row in rows:
                language = row["type"]
                versions_dict.setdefault(language, []).append(row)

            return versions_dict
    except sqlite3.Error as e:
        print(f"Lỗi database khi lấy danh sách phiên bản: {e}")
        raise e

def get_all_languages_settings():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(""" SELECT * FROM language_settings """)
            rows = cursor.fetchall()
            if rows:
                return [LanguageSetting(**dict(row)) for row in rows]
            return {}
    except sqlite3.Error as e:
        print("Lỗi khi lấy dữ liệu cấu hình language!")
        raise e

def update_language_settings(settings: LanguageSetting):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(""" UPDATE language_settings
                                SET selected_version = ?,
                                    executable_path  = ?,
                                    root_folder      = ?,
                                    is_ssl_enabled   = ?,
                                    is_chosen        = ?
                                WHERE language       = ?
            """,(
                settings.selected_version,
                settings.executable_path,
                settings.root_folder,
                settings.is_ssl_enabled,
                settings.is_chosen,
                settings.language,
            ))
            conn.commit()
            print("Cập nhật cấu hình language thành công",settings.language)
            return True
    except sqlite3.Error as e:
        print("Lỗi database khi cập nhật language!",settings.language)
        return False

def disable_all_languages():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE language_settings SET is_chosen = 0")
            conn.commit()
            return True
    except sqlite3.Error as e:
        return False