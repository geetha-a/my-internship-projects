import sys

class TodoItem:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def mark_item_as_completed(self, item):
        item.completed = True

    def update_item_description(self, item, new_description):
        item.description = new_description

    def update_item_due_date(self, item, new_due_date):
        item.due_date = new_due_date

    def update_item_priority(self, item, new_priority):
        item.priority = new_priority

    def display_items(self):
        for item in self.items:
            if item.completed:
                print(f"[X] {item.description}")
            else:
                print(f"[ ] {item.description}")

def main():
    to_do_list = TodoList()

    while True:
        print("To-Do List:")
        to_do_list.display_items()

        print("Command:")
        command = input()

        if command == "add":
            description = input("Task description: ")
            due_date = input("Due date (optional): ")
            priority = input("Priority (optional): ")

            to_do_list.add_item(TodoItem(description, due_date, priority))
        elif command == "complete":
            item_index = int(input("Item index to complete: "))
            item = to_do_list.items[item_index]

            to_do_list.mark_item_as_completed(item)
        elif command == "update":
            item_index = int(input("Item index to update: "))
            item = to_do_list.items[item_index]

            new_description = input("New task description: ")
            new_due_date = input("New due date (optional): ")
            new_priority = input("New priority (optional): ")

            if new_description is not None:
                to_do_list.update_item_description(item, new_description)

            if new_due_date is not None:
                to_do_list.update_item_due_date(item, new_due_date)

            if new_priority is not None:
                to_do_list.update_item_priority(item, new_priority)
        elif command == "remove":
            item_index = int(input("Item index to remove: "))
            item = to_do_list.items[item_index]

            to_do_list.remove_item(item)
        elif command == "quit":
            break

    print("Goodbye!")

if __name__ == "__main__":
    main()
