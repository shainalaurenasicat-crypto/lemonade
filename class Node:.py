class Node:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, student_id, name):
        new_node = Node(student_id, name)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        if self.head is None:
            print("No student records.")
            return

        current = self.head

        while current is not None:
            print(current.student_id, "-", current.name)
            current = current.next


students = LinkedList()

students.insert_end("2026-001", "Ana Santos")
students.insert_end("2026-002", "Mark Reyes")
students.insert_end("2026-003", "John Cruz")
