class DashboardManagement:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DashboardManagement, cls).__new__(cls)
            cls._instance._data = {}
        return cls._instance
    def set(self,key,value):
        self._instance._data[key] = value
    def get(self,key,value):
        return self._instance._data.get(key,value)