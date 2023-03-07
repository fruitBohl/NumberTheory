import matplotlib.pyplot as plt

def collatz(
    paths: list[tuple[list[int], int]], iterations_remaining: int
) -> list[tuple[list[int], int]]:
    if iterations_remaining == 0:
        min_value = 2^63 - 1
        min_path = []
        data = {}
        current_path = 1

        for (path, evens) in paths:
            data[f'path {current_path}'] = evens/51
            current_path += 1

            if evens <= min_value:
                min_value = evens
                min_path = path

        print(f"The minimum path is {min_path} with {min_value} evens.")

        values = list(data.values())
        plt.hist(values, bins=20)
        plt.show()

    else:
        paths = add_to_paths(paths)
        collatz(paths, iterations_remaining - 1)
        

def add_to_paths(paths: list[tuple[list[int], int]]) -> list[tuple[list[int], int]]:
    new_paths = []

    for (path, evens) in paths:
        endpoint = path[-1]
        new_path = path.copy()
        other_path = path.copy()
        new_path.append(endpoint * 2)
        
        if (new_path, evens+1) not in new_paths:
            new_paths.append((new_path, evens+1))
        
        if (endpoint % 3 == 1) & (endpoint > 4) & (endpoint % 2 == 0):
            new_evens = evens

            if (endpoint - 1 / 3) % 2 == 0:
                new_evens += 1

            other_path.append(int((endpoint - 1) / 3))
            
            if (other_path, new_evens) not in new_paths:
                new_paths.append((other_path, new_evens))

    return new_paths

def main():
    collatz([([1], 0)], 51)

if __name__ == "__main__":
    main()
