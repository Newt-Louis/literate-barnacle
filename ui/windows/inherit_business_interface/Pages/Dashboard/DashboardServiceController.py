class DashboardServiceController:
    def __init__(self):

    def on_save_changes(self):
        print("dashboards Page Controller _on_save_changes")

    def on_cancel_changes(self):
        print("dashboards Page Controller _on_cancel_changes")

    def on_add_new_data(self):
        print("dashboards Page Controller _on_add_new_data")

    def on_update_data(self):
        print("dashboards Page Controller _on_update_data")

    def on_load_data(self):
        print("dashboards Page Controller _on_load_data")

    def update_webserver_info(self, data: dict):
        print("dashboards Page Controller _update_webserver_info")