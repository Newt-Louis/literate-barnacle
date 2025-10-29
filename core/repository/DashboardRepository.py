import sqlite3
from core.config import config
from core.database.model.DashboardSetting import DashboardSetting

DB_PATH = config.DB_PATH

def get_all_dashboard_settings():
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dashboard_settings")
        rows = cursor.fetchall()

        if len(rows) is not 0:
            return [DashboardSetting(**dict(row)) for row in rows]
        return None
    except sqlite3.Error as e:
        print(e)
        raise

def save_webserver(webserver_info):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           UPDATE dashboard_settings
                           SET type    = ?,
                               version = ?
                           WHERE service = 'webserver'
                            """,(
                               webserver_info.type,
                               webserver_info.version,
                           ))
            conn.commit()
            print("Đã lưu thông tin webserver vào database")
            return True
    except Exception as e:
        print(e)
        return False

def save_database(database_info):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           UPDATE dashboard_settings
                           SET type    = ?,
                               version = ?
                           WHERE service = 'database'
                            """,(
                               database_info.type,
                               database_info.version,
                           ))
            conn.commit()
            print("Đã lưu thông tin database vào database")
            return True
    except Exception as e:
        print(e)
        return False

def save_language(language_info):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           UPDATE dashboard_settings
                           SET type    = ?,
                               version = ?
                           WHERE service = 'language'
                            """,(
                               language_info.type,
                               language_info.version,
                           ))
            conn.commit()
            print("Đã lưu thông tin language vào database")
            return True
    except Exception as e:
        print(e)
        return False

def save_tool(tool_info):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           UPDATE dashboard_settings
                           SET type    = ?,
                               version = ?
                           WHERE service = 'tool'
                            """,(
                               tool_info.type,
                               tool_info.version,
                           ))
            conn.commit()
            print("Đã lưu thông tin tool vào database")
            return True
    except Exception as e:
        print(e)
        return False

def save_network(network_info):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           UPDATE dashboard_settings
                           SET type    = ?,
                               version = ?
                           WHERE service = 'network'
                            """,(
                               network_info.type,
                               network_info.version,
                           ))
            conn.commit()
            print("Đã lưu thông tin network vào database")
            return True
    except Exception as e:
        print(e)
        return False

def save_serivce_statuses(services_info: dict):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.executemany("""
                           UPDATE dashboard_settings
                           SET is_running = ?
                           WHERE service = ?
                           """,
                           [(is_running, service_name) for service_name, is_running in services_info])
            conn.commit()
            print("Đã lưu trạng thái mới cho các dịch vụ")
            return True
    except Exception as e:
        print(e)
        return False