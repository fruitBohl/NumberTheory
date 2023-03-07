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
    elements_generated = []

    paths = add_nones(paths, 2 ** num_iterations)

    for count, element in enumerate(prev_generated_elems):
        element_index = paths.index(element)

        elements_generated.append(element * 2)
        paths[element_index+2**(num_iterations-iterations_remaining)+count] = element*2

        if (element % 6 == 4) & (element > 4):
            distance_from_prev_elem = 0
            if count>0:
                distance_from_prev_elem = element_index - paths.index(prev_generated_elems[count-1])

            elements_generated.append(int((element - 1) / 3))
            paths[element_index+2**(num_iterations-iterations_remaining)+(2*distance_from_prev_elem)+1] = (int((element - 1) / 3))

    print("paths", paths)
    print("elements generated", elements_generated)
    print("")

    return paths, elements_generated


def main():
    paths = collatz([1], 8, [1], 8)
    tree = build(paths)
    print(tree)


if __name__ == "__main__":
    main()
