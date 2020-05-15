from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # if first item add to head
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        # check to see if length is less than the capacity given
        elif len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.current.next

        else:
            # if next exist set current to next
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head
            self.current.value = item

    def get(self):
        # Note:  This is the only []
        list_buffer_contents = []
        get_list = self.storage.head
        # TODO: Your code here
        while get_list is not None:
            list_buffer_contents.append(get_list.value)
            get_list = get_list.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
