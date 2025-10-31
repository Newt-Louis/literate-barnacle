from core.services.languages import LanguageCoreService

class LanguagesServiceController:
    def __init__(self):
        self.language_core_service = LanguageCoreService()

    def save_changes(self):
        print("Languages Page Controller _on_save_changes")

    def cancel_changes(self):
        print("Languages Page Controller _on_cancel_changes")

    def add_new_data(self):
        print("Languages Page Controller _on_add_new_data")

    def update_data(self):
        print("Languages Page Controller _on_update_data")

    def load_data(self):
        try:
            data = self.language_core_service.load_settings()
            return None if data is None else data
        except Exception as e:
            print(e)
            raise