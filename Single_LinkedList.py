class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            raise ValueError("List is empty")
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next is None:
            raise ValueError(f"Value {value} not found in the list")
        current.next = current.next.next

    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False


# Example usage
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    # Insertions
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_beginning(5)
    print("List after insertions:", linked_list.traverse())

    # Search
    print("Search for 20:", linked_list.search(20))
    print("Search for 15:", linked_list.search(15))

    # Deletion
    linked_list.delete_by_value(10)
    print("List after deleting 10:", linked_list.traverse())

    # Edge cases
    linked_list.delete_by_value(5)
    print("List after deleting 5:", linked_list.traverse())
    linked_list.delete_by_value(20)
    print("List after deleting last element (20):", linked_list.traverse())
