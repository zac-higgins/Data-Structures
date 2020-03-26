# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
            return
        elif self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
                return
            else:
                self.left.insert(value)
        elif self.value <= value:
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None:
            return False
        elif self.value == target:
            return True
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value is not None:
            cb(self.value)
            if self.right is not None:
                self.right.for_each(cb)
            if self.left is not None:
                self.left.for_each(cb)
        return
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)
        return

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            # current_node = q.storage.tail.value
            current_node = q.dequeue()
            print(current_node.value)
            if current_node.left:
                q.enqueue(current_node.left)
            if current_node.right:
                q.enqueue(current_node.right)
        return

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)
        return


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # node left right
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # left right node
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.in_order_print(bst)
# bst.bft_print(bst)
# bst.dft_print(bst)