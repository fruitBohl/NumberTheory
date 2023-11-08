from binarytree import build, Node

# Notes about collatz tree
# anything above 3 mod 6 cannot be in a loop


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

    print(root)
