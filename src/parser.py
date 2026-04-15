def parse_input(file_path):
    costs = {}
    assignments = {}
    group_size = 1
    inputs = []
    outputs = []

    with open(file_path) as f:
        for line in f:
            parts = line.split()
            if not parts:
                continue

            if parts[0] == "C":
                costs[parts[1]] = int(parts[2])

            elif parts[0] == "G":
                group_size = int(parts[1])

            elif parts[0] == "I":
                inputs = list(map(int, parts[1:-1]))

            elif parts[0] == "O":
                outputs = list(map(int, parts[1:-1]))

            elif parts[0] == "A":
                aid = int(parts[1])
                assignments[aid] = {
                    "inputs": [int(parts[2]), int(parts[3])],
                    "output": int(parts[4]),
                    "food": parts[5]
                }

    return costs, group_size, inputs, outputs, assignments