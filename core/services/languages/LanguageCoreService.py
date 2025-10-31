from core.database.model import LanguageSetting
from core.repository import LanguageRepository

class LanguageCoreService:
    language_repository = LanguageRepository
    def __init__(self):
        pass

    def load_settings(self) -> list[LanguageSetting] | None:
        print(f"Language: Đang tải cấu hình...")
        try:
            settings_data = LanguageCoreService.language_repository.get_all_languages_settings()
            return None if settings_data is None else settings_data
        except:
            raise
