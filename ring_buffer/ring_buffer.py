class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # check if there is space in the storage
        if None in self.storage:
            # get the index of None
            emptyIndex = self.storage.index(None)
            self.storage[emptyIndex] = item
        # if storage is full
        else:
            # get the first element as the oldest
            oldestItem = self.storage[0]
            for i in self.storage:
                # getting the oldest element in the array
                if i < oldestItem:
                    oldestItem = i
            # get the oldest item index
            oldestItemIndex = self.storage.index(oldestItem)
            # override item with the oldest
            self.storage[oldestItemIndex] = item

    def get(self):
        return [item for item in self.storage if item != None]
