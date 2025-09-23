class LanguagesServiceController:
    def __init__(self, languages_model):
        self.languages_model = languages_model

    def _on_save_changes(self):
        print("Languages Page Controller _on_save_changes")

    def _on_cancel_changes(self):
        print("Languages Page Controller _on_cancel_changes")

    def _on_add_new_data(self):
        print("Languages Page Controller _on_add_new_data")

    def _on_update_data(self):
        print("Languages Page Controller _on_update_data")

    def _on_load_data(self):
        print("Languages Page Controller _on_load_data")