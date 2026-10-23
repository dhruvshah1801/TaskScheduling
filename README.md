# TASK SCHEDULING SYSTEM USING PYTHON

 1. Title Page

Project Title:Task Scheduling System Using Python

Subject: Python Programming

Submitted By: Dhruv Shah

Enrollment Number:12402080601031

Semester: 5th Semester

Department: Information Technology-A

## 2. Abstract

The Task Scheduling System is a Python-based application designed to create, manage, and execute tasks efficiently. The system provides a command-line interface through which users can add tasks, view task details, execute pending tasks, and monitor task statistics.

The main purpose of this project is to demonstrate three important Python programming concepts: functions, Object-Oriented Programming (OOP), and multithreading. Functions divide the application into reusable operations, OOP organizes task information using classes and objects, and multithreading allows multiple tasks to execute concurrently.

The application stores task information in memory using Python data structures. It does not require an external database or additional software libraries. This makes it suitable for learning and demonstrating fundamental Python programming concepts.

## 3. Introduction

Task scheduling is the process of organizing and executing tasks according to a defined plan. Task scheduling systems are useful in areas such as operating systems, project management, background processing, and automated workflows.

This project implements a basic task scheduling application using Python. Users can enter task details, assign a priority, specify a simulated execution duration, and execute pending tasks.

The system uses the `threading` module to demonstrate concurrent execution. Each task is assigned a separate thread, and the application waits for all threads to complete before returning to the main menu.

## 4. Problem Statement

Managing multiple tasks manually can be difficult when users need to track task details, execution status, and completion. A simple software application is required to organize tasks and demonstrate how multiple independent tasks can be processed concurrently.

The proposed system addresses this problem by providing a menu-driven interface, task management functionality, status tracking, and multithreaded execution.

## 5. Objectives

The main objectives are:

1. To develop a task management application using Python.
2. To implement functions for reusable program operations.
3. To apply OOP concepts through classes, objects, attributes, and methods.
4. To implement multithreading using Python's `threading` module.
5. To maintain task status throughout execution.
6. To validate user input and handle common errors.
7. To display task information and execution statistics.
8. To understand the advantages and limitations of in-memory storage.

## 6. Scope of the Project

The project supports:

- Creating tasks with names and descriptions.
- Assigning High, Medium, or Low priority.
- Specifying simulated task execution duration.
- Viewing all stored tasks.
- Executing pending tasks concurrently.
- Tracking Pending, Running, Completed, and Failed statuses.
- Displaying task statistics.
- Handling invalid input.

The current version is designed for educational purposes and does not include persistent storage, automatic execution at a specified clock time, or a graphical user interface.

## 7. Software and Hardware Requirements

### Software Requirements

- Operating System: Windows, Linux, or macOS
- Programming Language: Python 3
- Development Environment: Visual Studio Code or IDLE
- Python Modules: `threading` and `time`
- Storage: Python list and objects in memory

### Hardware Requirements

- A computer or laptop
- Minimum 2 GB RAM recommended
- A keyboard and display
- Sufficient disk space for Python and the source code

No additional Python packages or database installation is required.

## 8. System Design

The system is divided into the following components:

**1. User Interface Module:** Displays the menu and accepts user choices.

**2. Task Module:** Defines the `Task` class and stores individual task details.

**3. Scheduling Module:** Defines the `TaskScheduler` class and manages task creation, listing, execution, and statistics.

**4. Thread Execution Module:** Creates and starts separate threads for pending tasks.

**5. Input Validation Module:** Validates task names, priority, duration, and menu choices.

### System Workflow

Start the application → Display menu → Accept user choice → Add or view tasks, execute pending tasks, or view statistics → Return to menu → Exit.

## 9. Implementation of Major Python Concepts

### 9.1 Functions

Functions are used to divide the application into smaller, reusable operations. Examples include `main()`, `display_menu()`, `add_task_menu()`, and `get_duration()`.

They improve readability, reduce code duplication, and simplify testing.

### 9.2 Object-Oriented Programming

The project contains two main classes.

Task:Represents a task and stores its ID, name, description, priority, duration, and status.

TaskScheduler: Manages the collection of task objects and provides methods to add, display, execute, and count tasks.

The `__init__()` method initializes object attributes. The `self` keyword refers to the current object.

### 9.3 Multithreading

The project imports Python's `threading` module and creates a thread for each pending task.

The `start()` method begins thread execution, while `join()` waits for each thread to finish. The `Lock` object protects shared status updates.

Multithreading enables the independent tasks to run concurrently, reducing the total elapsed time for suitable workloads.

### 9.4 Exception Handling

The `try` and `except` statements handle invalid numeric input. This allows the program to request valid input again rather than terminating unexpectedly.

### 9.5 Data Structures

A Python list stores task objects. Each object contains attributes representing its details and current status. The data remains available while the application is running.

## 10. Algorithm

1. Start the program.
2. Create a `TaskScheduler` object.
3. Display the main menu.
4. Accept the user's choice.
5. If the choice is Add Task, collect task details, validate them, and create a task object.
6. If the choice is View Tasks, display all tasks and their statuses.
7. If the choice is Run Pending Tasks, identify pending tasks and mark them as Running.
8. Create a separate thread for each pending task.
9. Start all threads and wait for their completion.
10. Update task statuses and display the execution result.
11. If the choice is View Statistics, count tasks by status and display the totals.
12. If the choice is Exit, terminate the program.
13. Otherwise, display an invalid-choice message.
14. Repeat until the user exits.

## 11. Expected Results

The application successfully demonstrates task creation, task listing, multithreaded execution, task status updates, and execution statistics.

When multiple tasks are started, their execution messages may appear in different orders because thread scheduling is managed by the operating system.

The system also validates common input errors and handles an empty task list.

## 12. Limitations

- Tasks are stored only in memory.
- Task information is lost when the application closes.
- Task durations simulate execution using delays.
- Priority is stored and displayed but does not control execution order.
- Tasks start when the user selects the execution option; they are not automatically triggered by a clock schedule.
- The application is a basic command-line implementation.

## 13. Future Enhancements

The project can be extended by introducing:

1. SQLite database integration for permanent storage.
2. A Tkinter graphical user interface.
3. Automatic execution at scheduled dates and times.
4. Priority-based task ordering.
5. Task editing, deletion, and cancellation.
6. Execution logs and completion timestamps.
7. Notifications when tasks finish.
8. A controlled thread pool for managing large numbers of tasks.

## 14. Conclusion

The Task Scheduling System demonstrates the practical application of functions, Object-Oriented Programming, and multithreading in Python. It provides basic task management functionality through a command-line interface and illustrates how multiple independent tasks can execute concurrently.

The project also demonstrates input validation, exception handling, shared-data synchronization, and the use of Python data structures.

This implementation provides a foundation for developing more advanced scheduling applications with persistent storage, graphical interfaces, and automated scheduling capabilities.

## 15. References

1. Python Official Documentation — https://docs.python.org/3/
2. Python `threading` Module — https://docs.python.org/3/library/threading.html
3. Python `time` Module — https://docs.python.org/3/library/time.html
4. Python Classes and Objects — https://docs.python.org/3/tutorial/classes.html
