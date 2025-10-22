import sqlite3


def up(cursor: sqlite3.Cursor):
    print("Applying migration: create_webserver_table...")

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS webserver_settings
                   (
                       server_name        TEXT PRIMARY KEY,
                       selected_version   TEXT,
                       executable_path    TEXT,
                       sites_enabled_path TEXT,
                       tld_template       TEXT DEFAULT '.test',
                       http_port          INTEGER,
                       ssl_port           INTEGER
                   );
                   """)

    # Chèn dữ liệu mẫu
    cursor.execute(
        "INSERT OR IGNORE INTO webserver_settings (server_name, http_port, ssl_port) VALUES ('apache', 80, 443);")
    cursor.execute(
        "INSERT OR IGNORE INTO webserver_settings (server_name, http_port, ssl_port) VALUES ('nginx', 8080, 8443);")


# Hàm down để hoàn tác
def down(cursor: sqlite3.Cursor):
    print("Reverting migration: create_webserver_table...")
    cursor.execute("DROP TABLE IF EXISTS webserver_settings;")