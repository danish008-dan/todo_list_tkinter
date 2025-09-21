
# ---------------------- Import Required Libraries ----------------------
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pymysql

# ---------------------- Database Connection ----------------------
def connect_db():
    """Function to connect with MySQL database (XAMPP)"""
    return pymysql.connect(
        host="localhost",
        user="root",        # Default XAMPP username
        password="",        # Keep empty if no password is set
        database="todo_app" # Database name
    )

# ---------------------- Database Functions ----------------------
def insert_task(title, description, deadline):
    """Insert a new task into the database"""
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO tasks (title, description, deadline, status) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (title, description, deadline, "Pending"))
    conn.commit()
    conn.close()

def fetch_tasks():
    """Fetch all tasks from the database"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_task(task_id):
    """Update a task status to Completed"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status=%s WHERE id=%s", ("Completed", task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    """Delete a task from the database"""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()

# ---------------------- GUI Class ----------------------
class ToDoApp:
    def __init__(self, root):
        """Initialize the main application window"""
        self.root = root
        self.root.title("Calm To-Do List App")
        self.root.geometry("800x500")
        self.root.configure(bg="#f8f9fa")  # Calm light background

        # ---------------------- Title Label ----------------------
        title_label = tk.Label(
            self.root,
            text="My To-Do List",
            font=("Helvetica", 20, "bold"),
            bg="#f8f9fa",
            fg="#2c3e50"
        )
        title_label.pack(pady=10)

        # ---------------------- Input Frame ----------------------
        input_frame = tk.Frame(self.root, bg="#f8f9fa")
        input_frame.pack(pady=10)

        # Title input
        tk.Label(input_frame, text="Title:", font=("Arial", 12), bg="#f8f9fa").grid(row=0, column=0, padx=10, pady=5)
        self.title_entry = tk.Entry(input_frame, font=("Arial", 12), width=25)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        # Description input
        tk.Label(input_frame, text="Description:", font=("Arial", 12), bg="#f8f9fa").grid(row=1, column=0, padx=10, pady=5)
        self.desc_entry = tk.Entry(input_frame, font=("Arial", 12), width=25)
        self.desc_entry.grid(row=1, column=1, padx=10, pady=5)

        # Deadline input
        tk.Label(input_frame, text="Deadline (YYYY-MM-DD):", font=("Arial", 12), bg="#f8f9fa").grid(row=2, column=0, padx=10, pady=5)
        self.deadline_entry = tk.Entry(input_frame, font=("Arial", 12), width=25)
        self.deadline_entry.grid(row=2, column=1, padx=10, pady=5)

        # ---------------------- Buttons ----------------------
        btn_frame = tk.Frame(self.root, bg="#f8f9fa")
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="Add Task", font=("Arial", 12), bg="#27ae60", fg="white", width=12, command=self.add_task)
        add_btn.grid(row=0, column=0, padx=10)

        update_btn = tk.Button(btn_frame, text="Mark Completed", font=("Arial", 12), bg="#2980b9", fg="white", width=14, command=self.complete_task)
        update_btn.grid(row=0, column=1, padx=10)

        delete_btn = tk.Button(btn_frame, text="Delete Task", font=("Arial", 12), bg="#c0392b", fg="white", width=12, command=self.delete_task)
        delete_btn.grid(row=0, column=2, padx=10)

        refresh_btn = tk.Button(btn_frame, text="Refresh", font=("Arial", 12), bg="#8e44ad", fg="white", width=12, command=self.load_tasks)
        refresh_btn.grid(row=0, column=3, padx=10)

        # ---------------------- Task Table ----------------------
        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Description", "Deadline", "Status"), show="headings", height=10)
        self.tree.pack(pady=20, fill="x")

        # Define columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Deadline", text="Deadline")
        self.tree.heading("Status", text="Status")

        # Set column width
        self.tree.column("ID", width=40, anchor="center")
        self.tree.column("Title", width=150, anchor="center")
        self.tree.column("Description", width=200, anchor="center")
        self.tree.column("Deadline", width=120, anchor="center")
        self.tree.column("Status", width=100, anchor="center")

        # Load tasks initially
        self.load_tasks()

    # ---------------------- Functions for Buttons ----------------------
    def add_task(self):
        """Add task to the database"""
        title = self.title_entry.get()
        desc = self.desc_entry.get()
        deadline = self.deadline_entry.get()

        if title == "" or deadline == "":
            messagebox.showwarning("Input Error", "Please fill at least Title and Deadline!")
        else:
            insert_task(title, desc, deadline)
            messagebox.showinfo("Success", "Task added successfully!")
            self.load_tasks()

    def load_tasks(self):
        """Load all tasks into the Treeview table"""
        for i in self.tree.get_children():
            self.tree.delete(i)

        tasks = fetch_tasks()
        for task in tasks:
            self.tree.insert("", "end", values=task)

    def complete_task(self):
        """Mark selected task as completed"""
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Select Task", "Please select a task to mark as completed.")
            return
        task_id = self.tree.item(selected_item)["values"][0]
        update_task(task_id)
        messagebox.showinfo("Success", "Task marked as completed!")
        self.load_tasks()

    def delete_task(self):
        """Delete selected task"""
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Select Task", "Please select a task to delete.")
            return
        task_id = self.tree.item(selected_item)["values"][0]
        delete_task(task_id)
        messagebox.showinfo("Success", "Task deleted successfully!")
        self.load_tasks()

# ---------------------- Main Function ----------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
