from core.services.webservers import WebserverCoreService

class WebserverServiceController:
    def __init__(self, webserver_model):
        self.webserver_model = webserver_model

    def on_save_changes(self):
        print("Webserver Page Controller _on_save_changes")

    def on_cancel_changes(self):
        print("Webserver Page Controller _on_cancel_changes")

    def on_add_new_data(self):
        print("Webserver Page Controller _on_add_new_data")

    def on_update_data(self):
        print("Webserver Page Controller _on_update_data")

    def on_load_data(self,server_name):
        print("Webserver Page Controller on_load_data")
        return WebserverCoreService.load_settings(server_name)