# Flask Task Management System

This is a simple Task Management System built with Flask, a Python web framework. It allows users to perform CRUD operations (Create, Read, Update, Delete) on tasks, filter tasks by status and priority, and mark tasks as completed.

## Features

- **Create Task:** Add new tasks with a description, due date, priority level, and status (pending by default).
- **Read Tasks:** View a list of tasks with options to filter by status (pending or completed) and priority (low, medium, high).
- **Update Task:** Edit task details such as description, due date, priority, and status.
- **Delete Task:** Remove tasks from the system.
- **Mark Task as Completed:** Change the status of a task to completed.
- **Responsive Design:** The interface is designed to work well on both desktop and mobile devices.

## Prerequisites

- Python 3.x
- Flask
- Web browser

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Harshi1Shetty/Flask-task-manager.git

## Directory Structure

Flask-task-manager/
│
├── app.py                  # Main Flask application script
├
│
│
├── templates/              # Directory for HTML templates
│   ├── create_task.html    # HTML template for creating a new task
│   ├── index.html          # Main page displaying task list and filters
│   └── update_task.html    # HTML template for updating a task
