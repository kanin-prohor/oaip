import time

class Timer:
    def __enter__(self) -> 'Timer':
        self.start_time = time.time()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        execution_time = self.end_time - self.start_time
        print(f"Время выполнения: {execution_time:.2f} сек")
        return False