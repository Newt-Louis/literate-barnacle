from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from core.services import SynchronizationService
from core.config import config

class DirectoryChangeHandler(FileSystemEventHandler):
    def __init__(self, callback_function):
        self.callback = callback_function

    def on_created(self, event):
        if event.is_directory:
            print(f"Handler phát hiện sự kiện tạo mới: {event.src_path}")
            self.callback() # Gọi cho "chuyên gia"

    def on_deleted(self, event):
        if event.is_directory:
            print(f"Handler phát hiện sự kiện xóa: {event.src_path}")
            self.callback() # Gọi cho "chuyên gia"


def start_watching():
    observer = Observer()

    apache_handler = DirectoryChangeHandler(callback_function=SynchronizationService.sync_apache_versions)
    observer.schedule(apache_handler, str(config.APACHE_ROOT), recursive=False)

    nginx_handler = DirectoryChangeHandler(callback_function=SynchronizationService.sync_nginx_versions)
    observer.schedule(nginx_handler, str(config.NGINX_ROOT), recursive=False)

    # ... làm tương tự cho Redis, PHP, ...

    observer.start()
    return observer