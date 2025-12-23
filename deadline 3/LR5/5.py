class Task: 
    def __init__(self, description: str, priority: int) -> None:
        self.description = description
        self.priority = priority
class TaskManager:
    def __init__(self) -> None:
        self.tasks = []
    def add_task(self, description: str, priority: int) -> None:
        new_task = Task(description, priority)
        self.tasks.append(new_task)
    def show_tasks(self) -> None:
        if not self.tasks:
            print("Список задач пуст")
            return
        for task in self.tasks:
            print(f"{task.description} - {task.priority}")