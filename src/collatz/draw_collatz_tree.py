from binarytree import build, tree


def collatz(
    paths: list[list],
    iterations_remaining: int,
    num_prev_generated_elems: int,
    num_iterations: int,
) -> list[int]:
    if iterations_remaining > 0:
        paths, num_prev_generated_elems = add_to_paths(
            paths, num_prev_generated_elems, num_iterations, iterations_remaining
        )
        return collatz(
            paths, iterations_remaining - 1, num_prev_generated_elems, num_iterations
        )
    elif iterations_remaining == 0:
        return paths


def add_nones(paths: list[list[int]], num: int) -> list[list[int]]:
    num_nones = 0

    while num_nones != num:
        paths.append(None)
        num_nones += 1
    return paths


def add_to_paths(
    paths: list[int],
    num_prev_generated_elems: int,
    num_iterations: int,
    iterations_remaining: int,
) -> tuple[list[int], int]:
    elements_searched = 0
    index = 0
    num_generated_elems = 0

    reverse_paths = paths.copy()
    reverse_paths.reverse()

    print(reverse_paths)
    print(
        "number of iterations - iterations_remaining = ",
        (num_iterations - iterations_remaining),
    )

    if len(paths) == 1:
        previously_generated_elements = [1]
    else:
        previously_generated_elements = reverse_paths[
            (num_iterations - iterations_remaining) ** 2
            - num_prev_generated_elems : (num_iterations - iterations_remaining + 1)
            ** 2
        ]

    print(previously_generated_elements)

    while elements_searched < num_prev_generated_elems:
        if reverse_paths[index] == None:
            index += 1
            continue

        if num_prev_generated_elems > 1:
            paths = add_nones(paths, num_prev_generated_elems**2 - 2)
            paths.append(reverse_paths[index] * 2)
        else:
            paths.append(reverse_paths[index] * 2)

        if (reverse_paths[index] % 6 == 4) & (reverse_paths[index] > 4):
            paths.append(int((reverse_paths[index] - 1) / 3))
            num_generated_elems += 1
            paths = add_nones(
                paths, 2 ** (num_iterations - iterations_remaining + 1) - 2
            )
        else:
            paths = add_nones(
                paths, 2 ** (num_iterations - iterations_remaining + 1) - 1
            )
        index += 1
        elements_searched += 1
        num_generated_elems += 1

    return paths, num_generated_elems


def main():
    paths = collatz([1], 6, 1, 6)
    tree = build(paths)
    print(tree)


if __name__ == "__main__":
    main()
