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


def search_for_similar_pattern(
    depth: int, iteration: int, leaf: int, pattern_dict: Dict[List[str], List[int]]
) -> Dict[str, Optional[Node]]:
    """
    Given a certain depth d start leaf l, noting the pattern, and then look at all leaves
    and see if given the same depth, they also have the same pattern. Do this recursively for i
    iterations.
    """

    if iteration == 0:
        return pattern_dict

    # calculate pattern for current leaf
    paths, next_leaves = collatz([leaf], [leaf], depth, depth)
    pattern = create_pattern(paths)
    current_tree_pattern = build(pattern)

    # add pattern to list
    for pattern_leaf, tree_pattern in pattern_dict.items():
        if tree_pattern.values == current_tree_pattern.values:
            pattern_dict[pattern_leaf + f", {leaf}"] = pattern_dict.pop(pattern_leaf)
            break
    else:
        pattern_dict[f"leaf {leaf}"] = current_tree_pattern

    # calculate next leaves
    for new_leaf in next_leaves:
        return search_for_similar_pattern(depth, iteration - 1, new_leaf, pattern_dict)


if __name__ == "__main__":
    pattern_dict = search_for_similar_pattern(10, 2, 1, {})

    for leaf, pattern in pattern_dict.items():
        print(leaf)
        pattern.pprint()
