class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_value):
        for i, child in enumerate(self.children):
            if child.value == child_value:
                del self.children[i]
                return
        raise ValueError(f"Child with value {child_value} not found")

    def traverse(self):
        """Traverse the tree in a depth-first manner."""
        result = [self.value]
        for child in self.children:
            result.extend(child.traverse())
        return result


# Example Usage
if __name__ == "__main__":
    # Create root node
    root = TreeNode("Root")

    # Add children to the root
    child1 = TreeNode("Child1")
    child2 = TreeNode("Child2")
    root.add_child(child1)
    root.add_child(child2)

    # Add children to Child1
    child1_1 = TreeNode("Child1_1")
    child1_2 = TreeNode("Child1_2")
    child1.add_child(child1_1)
    child1.add_child(child1_2)

    # Add children to Child2
    child2_1 = TreeNode("Child2_1")
    child2.add_child(child2_1)

    # Traversal
    print("Tree traversal:", root.traverse())

    # Remove a child
    root.remove_child("Child2")
    print("Tree traversal after removing Child2:", root.traverse())
