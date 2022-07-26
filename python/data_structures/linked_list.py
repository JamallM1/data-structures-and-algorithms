class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None
        self.tail = None

    def __str__(self):
        text = ""
        current = self.head

        while current is not None:
            text += "{ " + str(current.value) + " } -> "
            print(txt)
            current = current.next
        return text + "NULL"

    def includes(self, target):
        current = self.head

        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):

        new_node = Node(value)

        # start at  the beginning or head
        current = self.head

        while current:
            # no next
            if not current.next:

                current.next = new_node

                break
            else:
                # moves to the next one
                current = current.next

    def insert_before(self, search_val, value):
        new_node = Node(value)

        if self.head.value == search_val:
            self.insert(value)
            return

        # start at head or beginning
        current = self.head

        while current and current.next:
            # if current node has a value it looks for value
            if current.next.value == search_val:

                new_node.next = current.next

                current.next = new_node

                break
            else:
                current = current.next

    def insert_after(self, search_val, value):

        current = self.head

        while current:
            if current.value == search_val:
                self.insert_before(current.next.value, value)
                return
            else:
                current = current.next


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
