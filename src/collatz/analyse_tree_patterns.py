from binarytree import build, Node
from typing import *
import numpy as np
from draw_collatz_tree import collatz


def get_leaves(prev_generated_elems: List[int]) -> List[int]:
    """
    Generates the next elements in the collatz tree
    """

    elements_generated = []

    for element in prev_generated_elems:
        elements_generated.append(element * 2)
        if (element % 6 == 4) & (element > 4):
            elements_generated.append(int((element - 1) / 3))

    return elements_generated


def create_pattern(paths: List[int]) -> List[int]:
    """
    Creates a generalized pattern of section of collatz tree defined in 'paths'
    """

    paths_array = np.array(paths)
    paths_array_updated = np.where(paths_array != None, "x", paths_array)
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
        Given a certain depth and root, the subtree of the certain depth is calculated,
        its generalized pattern is noted, and if it is a previous unseen pattern, add to
        the dictionary of patterns, and if it is already seen, append the root to the
        list of roots which start with this pattern. Do this recursively for
        num_iterations.
        """

        # calculate pattern for current leaf
        tree, next_roots = collatz([root], [root], depth, depth)
        current_pattern = create_pattern(tree, next_roots)

        # add pattern to list
        for pattern_key, pattern in pattern_map.items():
            if pattern.values == build(current_pattern).values:
                pattern_starts[pattern_key] = (
                    pattern_starts.pop(pattern_key) + f",{root}"
                )
                break
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
            for new_root in next_roots:
                search_for_similar_pattern(depth, num_iterations - 1, new_root)

    search_for_similar_pattern(depth, num_iterations, root)

    return pattern_map, pattern_starts


if __name__ == "__main__":
    depth = int(input("Enter depth of pattern you would like to analyze: "))
    num_iterations = int(input("Enter number of iterations: "))

    pattern_map, pattern_starts = generate_similar_pattern(depth - 1, num_iterations, 1)

    for pattern_key, nodes in pattern_starts.items():
        print(f"Nodes with pattern seen below: {nodes}")
        pattern_map[pattern_key].pprint()
