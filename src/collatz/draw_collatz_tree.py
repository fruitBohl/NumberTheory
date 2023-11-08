from binarytree import Node
import graphviz


def inorder_traversal(root: Node, dot):
    if root:
        inorder_traversal(root.left, dot)
        dot.node(str(root.value), label=str(root.value))
        if root.left:
            dot.edge(str(root.left.value), str(root.value), style="dotted")
        if root.right:
            dot.edge(str(root.value), str(root.right.value), style="dotted")
        inorder_traversal(root.right, dot)


def postorder_traversal(root: Node, dot):
    if root:
        postorder_traversal(root.left, dot)
        postorder_traversal(root.right, dot)
        dot.node(str(root.value), label=str(root.value))
        if root.left:
            dot.edge(str(root.left.value), str(root.value), style="dotted")
        if root.right:
            dot.edge(str(root.right.value), str(root.value), style="dotted")


def visualize_binary_tree(root: Node):
    dot_inorder = graphviz.Digraph(comment="Collatz Tree")
    postorder_traversal(root, dot_inorder)
    dot_inorder.render("collatz_tree", view=True, format="jpg")


def collatz(
    prev_generated_nodes: list[Node], iterations_remaining: int, num_iterations: int
) -> list[Node]:
    """
    Recursive function to generate breadth-first list representation of collatz tree of
    depth num_iterations.
    """

    if iterations_remaining > 0:
        prev_generated_nodes = add_to_tree(prev_generated_nodes, num_iterations)
        return collatz(prev_generated_nodes, iterations_remaining - 1, num_iterations)
    return


def add_to_tree(prev_generated_nodes: list[Node], num_iterations: int) -> list[Node]:
    """
    Adds another level to the breadth_first_representation of the collatz tree.
    """

    nodes_generated = []

    for node in prev_generated_nodes:
        new_double_node = Node(node.value * 2)
        node.left = new_double_node
        nodes_generated.append(new_double_node)

        if (node.value % 6 == 4) and (node.value > 4):
            new_odd_node = Node(int((node.value - 1) / 3))
            nodes_generated.append(new_odd_node)
            node.right = new_odd_node

    return nodes_generated


if __name__ == "__main__":
    depth = int(input("Enter depth of collatz tree you would like to visualize: "))
    start_pos = int(input("Enter number for bottom of collatz tree:"))

    root = Node(start_pos)

    collatz([root], depth - 1, depth - 1)

    visualize_binary_tree(root)
