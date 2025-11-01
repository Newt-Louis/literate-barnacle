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
            return None if settings_data is {} else settings_data
        except:
            raise

    def load_all_language_versions(self):
        try:
            languages_version_data = self.language_repository.get_all_language_versions()
            return None if languages_version_data is {} else languages_version_data
        except:
            raise
