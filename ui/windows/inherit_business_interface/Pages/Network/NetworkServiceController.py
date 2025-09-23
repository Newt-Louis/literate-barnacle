class NetworkServiceController:
    def __init__(self, network_model):
        self.network_model = network_model

    def _on_save_changes(self):
        print("Network Page Controller _on_save_changes")

    def _on_cancel_changes(self):
        print("Network Page Controller _on_cancel_changes")

    def _on_add_new_data(self):
        print("Network Page Controller _on_add_new_data")

    def _on_update_data(self):
        print("Network Page Controller _on_update_data")

    def _on_load_data(self):
        print("Network Page Controller _on_load_data")