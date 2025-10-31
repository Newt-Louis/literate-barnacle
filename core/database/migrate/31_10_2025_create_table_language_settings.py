import sqlite3

def up(cursor: sqlite3.Cursor):
    print("Applying migration: create_language_settings_table...")

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS language_settings (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       language TEXT,
                       selected_version TEXT,
                       is_ssl_enabled INTEGER NOT NULL  default 0,
                       root_folder TEXT
                   );
                   """)
    # Chèn dữ liệu mẫu
    cursor.execute("INSERT OR IGNORE INTO language_settings (language, selected_version, root_folder) VALUES ('PHP', 'php-8.2.29-nts-Win32-vs16-x64', 'D:\php-8.2.29-nts-Win32-vs16-x64');")
    cursor.execute("INSERT OR IGNORE INTO language_settings (language, selected_version, root_folder) VALUES ('Python', 'python-3.13.3-amd64', 'D:\Python313');")
    cursor.execute("INSERT OR IGNORE INTO language_settings (language, selected_version, root_folder) VALUES ('Java', 'jdk-21', 'D:\jdk-21');")
    cursor.execute("INSERT OR IGNORE INTO language_settings (language, selected_version, root_folder) VALUES ('Nodejs', 'node-v24.11.0-win-x64', 'D:\node-v24.11.0-win-x64');")

# Hàm down để hoàn tác
def down(cursor: sqlite3.Cursor):
    print("Reverting migration: create_language_settings_table...")
    cursor.execute("DROP TABLE IF EXISTS language_settings;")