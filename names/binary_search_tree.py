class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is smaller than the current value
        if value < self.value:
            # if there is no left
            if not self.left:
                self.left = BinarySearchTree(value)
            # otherwize insert in the left
            else:
                self.left.insert(value)
        # check if the value is bigger then the current value
        if value > self.value:
            # if there is no right
            if not self.right:
                self.right = BinarySearchTree(value)
            # otherwise insert it
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if the value is the target
        if self.value == target:
            return True

        # check if the target is smaller the value
        if target < self.value:
            # if there is no value in the left
            if not self.left:
                return False
            # recursive call the function again
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right is not None:
            max = self.value
            self = self.right

        max = self.value
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

   