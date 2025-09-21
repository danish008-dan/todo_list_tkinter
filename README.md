# todo_list_tkinter


Overview

This project is a To-Do List Desktop Application built using Python (Tkinter for GUI) and MySQL (via XAMPP) for database management.
It provides a simple and elegant interface with a calm light theme where users can:

Add new tasks

View tasks in a structured table

Mark tasks as completed

Delete tasks

Refresh the task list

🚀 Features

✔️ GUI built with Tkinter (clean & calm light theme)
✔️ CRUD operations (Create, Read, Update, Delete) on tasks
✔️ MySQL Database integration (XAMPP)
✔️ TreeView Table to display all tasks
✔️ Input fields for Title, Description, and Deadline
✔️ Color-coded action buttons

🛠️ Tech Stack

Python 3.x

Tkinter (GUI)

PyMySQL (Database connection)

MySQL via XAMPP

📂 Database Setup (MySQL – XAMPP)

Open phpMyAdmin (http://localhost/phpmyadmin
).

Create a new database:

CREATE DATABASE todo_app;


Select the database and create a table:

USE todo_app;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    deadline DATE,
    status ENUM('Pending', 'Completed') DEFAULT 'Pending'
);

▶️ How to Run

Clone this repository:

git clone https://github.com/your-username/todo-tkinter-mysql.git


Install required library:

pip install pymysql


Run the application:

python main.py

🎨 UI Preview

✅ Calm light background
✅ Structured task table
✅ Modern button colors (Green, Blue, Red, Purple)


Main Window with task list

Add task example

Completed task marked

📖 Future Enhancements

Add search functionality

Add task priority levels

Export tasks to CSV/Excel

Notifications for deadlines
