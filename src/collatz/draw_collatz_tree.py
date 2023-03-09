from binarytree import build


def collatz(
    breadth_first_representation: list[list],
    prev_generated_elems: list[int],
    iterations_remaining: int,
    num_iterations: int,
) -> list[int]:
    """
    Recursive function to generate breadth-first list representation of collatz tree of
    depth num_iterations.
    """

    if iterations_remaining > 0:
        breadth_first_representation, prev_generated_elems = add_to_tree(
            breadth_first_representation, prev_generated_elems, num_iterations
        )
        return collatz(
            breadth_first_representation,
            prev_generated_elems,
            iterations_remaining - 1,
            num_iterations,
        )
    elif iterations_remaining == 0:
        return breadth_first_representation


def add_nones(paths: list[int], num: int) -> list[list[int]]:
    """
    Simply appends 'num' None elements to the list.
    """

    num_nones = 0
    if num < 0:
        num = 0

    while num_nones != num:
        paths.append(None)
        num_nones += 1
    return paths


def add_to_tree(
    breadth_first_representation: list[int],
    prev_generated_elems: list[int],
    num_iterations: int,
) -> tuple[list[int], list[int]]:
    """
    Adds another level to the breadth_first_representation of the collatz tree.
    """
    elements_generated = []

    breadth_first_representation = add_nones(
        breadth_first_representation, 2**num_iterations
    )

    for element in prev_generated_elems:
        element_index = breadth_first_representation.index(element)
        elements_generated.append(element * 2)

        if element_index == 0:
            breadth_first_representation[1] = element * 2
        elif element_index == 1:
            breadth_first_representation[3] = element * 2
        else:
            breadth_first_representation[element_index * 2 + 1] = element * 2

        if (element % 6 == 4) & (element > 4):
            elements_generated.append(int((element - 1) / 3))
            breadth_first_representation[element_index * 2 + 2] = int((element - 1) / 3)

    return breadth_first_representation, elements_generated


def main():
    depth = input("Enter depth of collatz tree you would like to visualize: ")
    paths = collatz([1], [1], int(depth) - 1, int(depth) - 1)
    tree = build(paths)
    tree.pprint()


if __name__ == "__main__":
    main()
