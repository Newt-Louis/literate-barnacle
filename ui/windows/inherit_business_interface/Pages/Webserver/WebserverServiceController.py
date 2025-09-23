class WebserverServiceController:
    def __init__(self, webserver_model):
        self.webserver_model = webserver_model

    def _on_save_changes(self):
        print("Webserver Page Controller _on_save_changes")

    def _on_cancel_changes(self):
        print("Webserver Page Controller _on_cancel_changes")

    def _on_add_new_data(self):
        print("Webserver Page Controller _on_add_new_data")

    def _on_update_data(self):
        print("Webserver Page Controller _on_update_data")

    def _on_load_data(self):
        print("Webserver Page Controller _on_load_data")