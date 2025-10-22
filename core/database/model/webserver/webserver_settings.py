import sqlite3

DB_PATH = 'database/config.db'

def get_webserver_settings(server_name):
    """Lấy tất cả cài đặt cho một web server."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Trả về kết quả dạng dict-like
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM webserver_settings WHERE server_name = ?", (server_name,))
    settings = cursor.fetchone()
    conn.close()
    return dict(settings) if settings else None

def update_webserver_settings(server_name, settings_dict):
    """Cập nhật cài đặt cho một web server."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE webserver_settings
    SET selected_version = ?, http_port = ?, ssl_port = ?
    WHERE server_name = ?
    """, (
        settings_dict.get('selected_version'),
        settings_dict.get('http_port'),
        settings_dict.get('ssl_port'),
        server_name
    ))
    conn.commit()
    conn.close()