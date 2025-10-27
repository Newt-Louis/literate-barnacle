from core.services.webservers import WebserverCoreService

class WebserverServiceController:
    def __init__(self):
        self.webserver_core_service = WebserverCoreService()

    def save_changes(self):
        print("Webserver Page Controller _on_save_changes")

    def cancel_changes(self):
        print("Webserver Page Controller _on_cancel_changes")

    def add_new_data(self):
        print("Webserver Page Controller _on_add_new_data")

    def update_data(self):
        print("Webserver Page Controller _on_update_data")

    def load_data(self,server_name):
        print("Webserver Page Controller on_load_data")
        return self.webserver_core_service.load_settings(server_name)

    def load_webservers_version(self):
        return self.webserver_core_service.load_webservers_versions()