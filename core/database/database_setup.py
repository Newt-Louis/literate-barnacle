import sqlite3, os, importlib.util
from core.config import config

DB_PATH = config.DB_PATH
MIGRATIONS_DIR = config.MIGRATIONS_DIR

def run_migrations():
    """Hàm chính để chạy tất cả các migration cần thiết."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Tạo bảng theo dõi phiên bản nếu chưa có
    cursor.execute("""CREATE TABLE IF NOT EXISTS schema_version ('
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT NOT NULL UNIQUE,
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   ');""")
    conn.commit()

    # 2. Lấy danh sách các migration đã được áp dụng từ DB
    cursor.execute("SELECT filename FROM schema_version;")
    applied_migrations = {row[0] for row in cursor.fetchall()}

    # 3. Quét thư mục migrate để tìm tất cả các file migration
    migration_files = sorted(
        f for f in os.listdir(MIGRATIONS_DIR) if f.endswith('.py') and f != '__init__.py'
    )

    # 4. Lặp qua các file và chạy những file chưa được áp dụng
    for filename in migration_files:
        if filename not in applied_migrations:
            print(f"Found new migration: {filename}")

            try:
                # Import module từ file một cách linh hoạt
                module_path = MIGRATIONS_DIR / filename
                spec = importlib.util.spec_from_file_location(filename, module_path)
                migration_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(migration_module)

                # Gọi hàm up() trong file migration đó
                migration_module.up(cursor)

                # Nếu thành công, ghi lại vào bảng migrations
                cursor.execute("INSERT INTO schema_version (filename) VALUES (?)", (filename,))
                conn.commit()
                print(f"Successfully applied migration: {filename}")

            except Exception as e:
                print(f"ERROR applying migration {filename}: {e}")
                conn.rollback()  # Hoàn tác nếu có lỗi
                conn.close()
                return  # Dừng lại ngay lập tức

    print("All migrations are up to date.")
    conn.close()