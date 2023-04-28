from binarytree import build, Node
from typing import *
import numpy as np
from draw_collatz_tree import collatz, add_nones


def get_leaves(prev_generated_elems: List[int]) -> List[int]:
    """
    Adds another level to the breadth_first_representation of the collatz tree.
    """

    elements_generated = []

    for element in prev_generated_elems:
        elements_generated.append(element * 2)
        if (element % 6 == 4) & (element > 4):
            elements_generated.append(int((element - 1) / 3))

    return elements_generated


def create_pattern(paths: List[int]) -> List[int]:
    """Creates a generalized pattern of section of collatz tree defined in 'paths'"""

    paths_array = np.array(paths)

    paths_array_updated = np.where(paths_array != None, 1, paths_array)
    pattern = list(paths_array_updated)

    return pattern


def generate_similar_pattern(
    depth: int, num_iterations: int, root: int
) -> Tuple[Dict[int, Optional[Node]], Dict[int, str]]:
    pattern_map = {}
    pattern_starts = {}

    if (num_iterations <= 0) or (depth <= 0):
        return pattern_map, pattern_starts

    def search_for_similar_pattern(depth: int, num_iterations: int, root: int) -> None:
        """
        Given a certain depth d start leaf l, noting the pattern, and then look at all
        leaves and see if given the same depth, they also have the same pattern. Do this
        recursively for i iterations.
        """

        # calculate pattern for current leaf
        paths, next_leaves = collatz([root], [root], depth, depth)
        current_pattern = create_pattern(paths)

        # add pattern to list
        for pattern_key, pattern in pattern_map.items():
            if pattern.values == build(current_pattern).values:
                pattern_starts[pattern_key] = (
                    pattern_starts.pop(pattern_key) + f", {root}"
                )
        else:
            if pattern_starts == {}:
                new_pattern_key = 0
            else:
                new_pattern_key = max(list(pattern_starts.keys())) + 1
            pattern_map[new_pattern_key] = build(current_pattern)
            pattern_starts[new_pattern_key] = f"{root}"

        if num_iterations == 0:
            return
        else:
            for new_leaf in next_leaves:
                search_for_similar_pattern(depth, num_iterations - 1, new_leaf)

    search_for_similar_pattern(depth, num_iterations, root)

    return pattern_map, pattern_starts


if __name__ == "__main__":
    pattern_map, pattern_starts = generate_similar_pattern(2, 3, 1)

    for pattern_key, nodes in pattern_starts.items():
        print(f"leaves with pattern seen below: {nodes}")
        pattern_map[pattern_key].pprint()
