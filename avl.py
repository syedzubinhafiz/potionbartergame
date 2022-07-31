""" AVL Tree implemented on top of the standard BST. """

__author__ = 'Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from bst import BinarySearchTree
from typing import TypeVar, Generic
from node import AVLTreeNode

K = TypeVar('K')
I = TypeVar('I')


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ Self-balancing binary search tree using rebalancing by sub-tree
        rotations of Adelson-Velsky and Landis (AVL).
    """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """
        BinarySearchTree.__init__(self)

    def get_height(self, current: AVLTreeNode) -> int:
        """
            Get the height of a node. Return current.height if current is
            not None. Otherwise, return 0.
            :complexity: O(1)
        """

        if current is not None:
            return current.height
        return 0

    def get_balance(self, current: AVLTreeNode) -> int:
        """
            Compute the balance factor for the current sub-tree as the value
            (right.height - left.height). If current is None, return 0.
            :complexity: O(1)
        """

        if current is None:
            return 0
        return self.get_height(current.right) - self.get_height(current.left)

    def insert_aux(self, current: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert
            it. After insertion, performs sub-tree rotation whenever it becomes
            unbalanced.
            returns the new root of the subtree.
        """

        if current is None:
            current = AVLTreeNode(key, item)
            self.length += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)

        elif key > current.key:
            current.rightCount = current.rightCount + 1
            current.right = self.insert_aux(current.right, key, item)
        else:
            raise ValueError("Inserting duplicate item")
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        return self.rebalance(current)

    def delete_aux(self, current: AVLTreeNode, key: K) -> AVLTreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete. After deletion,
            performs sub-tree rotation whenever it becomes unbalanced.
            returns the new root of the subtree.
        """
        if current is None:
            raise ValueError(" Nothing to delete at targeted node ")

            # If the key to be deleted
            # is smaller than the current node's
            # key then it lies in  left subtree
        elif key < current.key:
            current.left = self.delete_aux(current.left, key)

            # If the key to be deleted
            # is greater than the current node's key
            # then it lies in right subtree
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
            current.rightCount -= 1
        else:
            # Node with only one child or no child
            if current.left is None:
                temp = current.right
                self.length -= 1
                # current.rightCount -= 1
                return temp

            elif current.right is None:
                temp = current.left
                self.length -= 1
                return temp

            # Node with two children:
            # Get the successor
            # (smallest in the right subtree)
            temp = self.get_minimal(current.right)

            # Copy the inorder successor's
            # content to this node
            current.key = temp.key
            current.item = temp.item

            # Delete the successor
            current.right = self.delete_aux(current.right, temp.key)
            current.rightCount -= 1

        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        current = self.rebalance(current)
        return current

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform left rotation of the sub-tree.
            Right child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                 current   10                                    child
                /       \                                      /     \
           l-tree     child   5        -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree    3             l-tree     center

            :complexity: O(1)
        """
        # Assign nodes in the present state
        child = current.right
        center = child.left

        # perform rotation
        current.right = center
        child.left = current

        # update height of current node and child node and return
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        child.height = 1 + max(self.get_height(child.left), self.get_height(child.right))
        # rightCount will now be the current node's rightCount - root - child's rightCount as current's right child now
        # is center
        current.rightCount = current.rightCount - 1 - child.rightCount
        return child

    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform right rotation of the sub-tree.
            Left child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                       current                                child
                      /       \                              /     \
                  child      r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree

            :complexity: O(1)
        """
        # Assign nodes as presently seen
        child = current.left
        center = child.right

        # Perform rotations
        current.left = center
        child.right = current
        # Update height of both parent and child,then return
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        child.height = 1 + max(self.get_height(child.left), self.get_height(child.right))

        # child's rightCount will now be child's rightCount (current) + current's rightCount (r-tree) + root
        child.rightCount = child.rightCount + current.rightCount + 1
        return child

    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate
            returns the new root of the subtree.
        """
        if self.get_balance(current) >= 2:
            child = current.right
            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)
            return self.left_rotate(current)

        if self.get_balance(current) <= -2:
            child = current.left
            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)
            return self.right_rotate(current)
        return current

    def kth_largest(self, k: int) -> AVLTreeNode:
        """
        Returns the kth largest element in the tree.
        k=1 would return the largest.
        The algorithm below works at O(log(N)) time complexity, since the operations don't increase linearly with the
        increase of size of input. This is possible because we're only traversing the right-subtrees and using the
        number of times the right-nodes are visited to determine kth largest node.
        """

        return self.kth_largest_aux(self.root, k)

    def kth_largest_aux(self, current: AVLTreeNode, k: int) -> AVLTreeNode:

        # if k is greater than the number of elements in the tree, it will raise a ValueError
        if k > self.length:
            raise ValueError("There are no " + str(k) + "th largest item in the tree")
        else:
            # if k is the same as the current rightCount we return that node
            if k == current.rightCount + 1:
                return current
            # if k is greater than the rightCount, it must lie on the left subtree.
            if k > current.rightCount + 1:
                return self.kth_largest_aux(current.left, k - 1 - current.rightCount)
            # if k is smaller than the rightCount, it must lie on the right subtree.
            if k < current.rightCount + 1:
                return self.kth_largest_aux(current.right, k)


if __name__ == '__main__':
    b = AVLTree()
    b[15] = "A"
    b[10] = "B"
    b[20] = "C"
    b[17] = "D"
    b[5] = "E"
    b[3] = "F"
    b[4] = "G"
    b[22] = "H"
    for i in range(b.__len__()):
        print(b.kth_largest(3).key)
        print(b.kth_largest(2).rightCount)
        # b.draw()
        # b.__delitem__(b.kth_largest(3).key)
        # b.draw()
