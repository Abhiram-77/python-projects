import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List App")

        self.tasks = []
        self.task_var = tk.StringVar()

        # GUI elements
        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(master, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=2, column=0, padx=10, pady=10)

        self.mark_done_button = tk.Button(master, text="Mark as Done", command=self.mark_done)
        self.mark_done_button.grid(row=2, column=1, padx=10, pady=10)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.task_var.set("")
            messagebox.showinfo("Task Added", f'Task "{task}" added successfully.')
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks found.")
        else:
            for task in self.tasks:
                status = "Done" if task["done"] else "Not Done"
                self.task_listbox.insert(tk.END, f'{task["task"]} - {status}')

    def mark_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index]["done"] = True
            self.view_tasks()
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as done.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            removed_task = self.tasks.pop(task_index)
            messagebox.showinfo("Task Removed", f'Task "{removed_task["task"]}" removed.')
            self.view_tasks()
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to remove.")


def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
