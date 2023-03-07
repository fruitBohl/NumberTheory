from binarytree import build, tree


def collatz(
    paths: list[list],
    iterations_remaining: int,
    prev_generated_elems: list[int],
    num_iterations: int,
) -> list[int]:
    if iterations_remaining > 0:
        paths, prev_generated_elems = add_to_paths(
            paths, prev_generated_elems, num_iterations, iterations_remaining
        )
        return collatz(
            paths, iterations_remaining - 1, prev_generated_elems, num_iterations
        )
    elif iterations_remaining == 0:
        return paths


def add_nones(paths: list[list[int]], num: int) -> list[list[int]]:
    num_nones = 0
    if num < 0:
        num = 0

    while num_nones != num:
        paths.append(None)
        num_nones += 1
    return paths


def add_to_paths(
    paths: list[int],
    prev_generated_elems: list[int],
    num_iterations: int,
    iterations_remaining: int,
) -> tuple[list[int], list[int]]:
    elements_searched = 0
    index = 0
    num_generated_elems = 0
    elements_generated = []

    for count, element in enumerate(prev_generated_elems):
        element_index = paths.index(element)
        if count == 0:
            paths = add_nones(paths, 2 ** (num_iterations - iterations_remaining) - 1)
        paths.append(element * 2)
        elements_generated.append(element * 2)

        if (element % 6 == 4) & (element > 4):
            paths.append(int((element - 1) / 3))
            elements_generated.append(int((element - 1) / 3))
        elif count != 0:
            paths.append(None)

    print("paths", paths)
    print("elements generated", elements_generated)
    print("")

    return paths, elements_generated


def main():
    paths = collatz([1], 8, [1], 8)
    print(paths)
    tree = build(paths)
    print(tree)


if __name__ == "__main__":
    main()
