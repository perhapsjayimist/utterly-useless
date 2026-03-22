import easier_json


class TaskManager:
    def __init__(self, name: str):
        self.name = name
        self.tasks = easier_json.load(name)
    
    def print(self):
        print(f"{self.name}: {self.name}")

        if not self.tasks:
            print("    No tasks! Use 'add' to add a task.")

        for i, task in enumerate(self.tasks):
            print(f"    {i} - {task}")

    def modify(self, new_tasks: list):
        self.tasks = new_tasks
        easier_json.save(self.name, self.tasks)

    def add(self, text: str, index: int = 0):
        self.tasks.insert(index, text)
        self.modify(self.tasks)

        print(f"Added task '{text}' at index {index}")

    def remove(self, index: int):
        text = self.tasks[index]

        self.tasks.pop(index)
        self.modify(self.tasks)

        print(f"Removed task '{text}' at index {index}")