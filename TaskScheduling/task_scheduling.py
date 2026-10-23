
import threading
import time


class Task:
    """Represents a single task."""

    def __init__(self, task_id, name, description, priority, duration):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.priority = priority
        self.duration = duration
        self.status = "Pending"


class TaskScheduler:
    """Manages tasks and executes them using threads."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.lock = threading.Lock()

    def add_task(self, name, description, priority, duration):
        """Create and store a new task."""
        task = Task(
            self.next_id, name, description, priority, duration
        )
        self.tasks.append(task)
        self.next_id += 1

        print(f"\nTask '{name}' added successfully!")
        print(f"Task ID: {task.task_id}")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("\nNo tasks found. Please add a task first.")
            return

        print("\n" + "=" * 85)
        print(f"{'ID':<5}{'Task Name':<22}{'Priority':<12}"
              f"{'Duration':<12}{'Status':<15}")
        print("=" * 85)

        for task in self.tasks:
            print(
                f"{task.task_id:<5}"
                f"{task.name[:20]:<22}"
                f"{task.priority:<12}"
                f"{task.duration:<12}"
                f"{task.status:<15}"
            )

        print("=" * 85)

    def execute_task(self, task):
        """Function executed by an individual thread."""
        try:
            print(
                f"[{threading.current_thread().name}] "
                f"{task.name} started."
            )

            # Simulate the time needed to complete the task.
            time.sleep(task.duration)

            with self.lock:
                task.status = "Completed"

            print(
                f"[{threading.current_thread().name}] "
                f"{task.name} completed."
            )

        except Exception as error:
            with self.lock:
                task.status = "Failed"
            print(f"Task '{task.name}' failed: {error}")

    def run_pending_tasks(self):
        """Run all pending tasks concurrently."""
        with self.lock:
            pending_tasks = [
                task for task in self.tasks
                if task.status == "Pending"
            ]

            if not pending_tasks:
                print("\nNo pending tasks to execute.")
                return

            # Mark tasks as Running before starting threads.
            for task in pending_tasks:
                task.status = "Running"

        threads = []

        print("\nStarting pending tasks...\n")

        for task in pending_tasks:
            thread = threading.Thread(
                target=self.execute_task,
                args=(task,),
                name=f"Thread-{task.task_id}"
            )
            threads.append(thread)
            thread.start()

        # Wait until all task threads finish.
        for thread in threads:
            thread.join()

        print("\nAll pending tasks have been processed.")

    def show_statistics(self):
        """Display task counts by status."""
        total = len(self.tasks)
        pending = sum(
            1 for task in self.tasks
            if task.status == "Pending"
        )
        running = sum(
            1 for task in self.tasks
            if task.status == "Running"
        )
        completed = sum(
            1 for task in self.tasks
            if task.status == "Completed"
        )
        failed = sum(
            1 for task in self.tasks
            if task.status == "Failed"
        )

        print("\n========== TASK STATISTICS ==========")
        print(f"Total tasks     : {total}")
        print(f"Pending tasks   : {pending}")
        print(f"Running tasks   : {running}")
        print(f"Completed tasks : {completed}")
        print(f"Failed tasks    : {failed}")
        print("=====================================")


def get_non_empty_input(message):
    """Accept input that is not empty."""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_duration():
    """Accept a valid task duration in seconds."""
    while True:
        try:
            duration = float(
                input("Enter duration in seconds (0 or more): ")
            )

            if duration >= 0 and duration < float("inf"):
                return duration

            print("Duration must be a finite, non-negative number.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def add_task_menu(scheduler):
    """Collect task details from the user."""
    print("\n---------- ADD NEW TASK ----------")

    name = get_non_empty_input("Enter task name: ")
    description = get_non_empty_input("Enter task description: ")

    while True:
        priority = input(
            "Enter priority (High/Medium/Low): "
        ).strip().capitalize()

        if priority in ["High", "Medium", "Low"]:
            break

        print("Please enter High, Medium, or Low.")

    duration = get_duration()

    scheduler.add_task(name, description, priority, duration)


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("       TASK SCHEDULING SYSTEM")
    print("=" * 40)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Run Pending Tasks")
    print("4. View Task Statistics")
    print("5. Exit")
    print("=" * 40)


def main():
    """Main function of the application."""
    scheduler = TaskScheduler()

    print("Welcome to the Task Scheduling System!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task_menu(scheduler)

        elif choice == "2":
            scheduler.view_tasks()

        elif choice == "3":
            scheduler.run_pending_tasks()

        elif choice == "4":
            scheduler.show_statistics()

        elif choice == "5":
            print("\nThank you for using the Task Scheduling System!")
            break

        else:
            print("\nInvalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()
