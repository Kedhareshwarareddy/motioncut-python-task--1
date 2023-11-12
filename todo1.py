import tkinter as tk

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        self.create_widgets()
        
    def create_widgets(self):
        # Task Entry Fields
        self.description_label = tk.Label(self.root, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack()

        self.due_date_label = tk.Label(self.root, text="Due Date:")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(self.root)
        self.due_date_entry.pack()

        self.priority_label = tk.Label(self.root, text="Priority:")
        self.priority_label.pack()
        self.priority_entry = tk.Entry(self.root)
        self.priority_entry.pack()

        # Task List
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_listbox.pack()

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack()

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        # Initialize List
        self.update_listbox()

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        self.update_listbox()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_listbox()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]].completed = True
            self.update_listbox()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            description = self.description_entry.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_entry.get()
            task = self.tasks[selected_index[0]]
            task.description = description
            task.due_date = due_date
            task.priority = priority
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task.completed else "Not Completed"
            self.task_listbox.insert(tk.END, f"{task.description} (Due: {task.due_date}, Priority: {task.priority}, Status: {status})")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
if __name__=='__main__':
    main()
