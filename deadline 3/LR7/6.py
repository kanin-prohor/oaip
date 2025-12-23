class DatabaseConfig:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, db_name: str = "", user: str = "", password: str = ""):
        if not hasattr(self, '_initialized'):
            self.db_name = db_name
            self.user = user
            self.password = password
            self._initialized = True

if __name__ == "__main__":
    config1 = DatabaseConfig("my_db", "admin", "secret")
    config2 = DatabaseConfig("another_db", "user", "123")
    
    print(config1 is config2)
    print(config1.db_name)
    print(config2.db_name)