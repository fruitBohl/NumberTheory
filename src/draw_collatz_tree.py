from binarytree import tree, Node


def collatz(paths: list[list[int]], iterations_remaining: int) -> list[list[int]]:
    if iterations_remaining > 0:
        paths = add_to_paths(paths)
        return collatz(paths, iterations_remaining - 1)
    elif iterations_remaining == 0:
        return paths


def add_to_paths(paths: list[list[int]]) -> list[list[int]]:
    new_paths = paths.copy()

    new_path = []
    for element in paths[-1]:
        new_path.append(element * 2)

        if (element % 6 == 4) & (element > 4):
            new_path.append(int((element - 1) / 3))
    new_paths.append(new_path)
    return new_paths


def main():
    paths = collatz([[1]], 10)

    for path in paths:
        print(path)


if __name__ == "__main__":
    main()


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.right = Node(4)
# root.left.right.left = Node(5)

# print(root)
