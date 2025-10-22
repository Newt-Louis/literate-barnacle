from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.resolve()

DB_PATH = PROJECT_ROOT / "core" / "database" / "sqlite.db"

MIGRATIONS_DIR = PROJECT_ROOT / "core" / "database" / "migrate"