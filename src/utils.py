from collections import defaultdict

def build_dependency_graph(assignments):

    output_to_assignment = {}
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for aid, data in assignments.items():
        output_to_assignment[data["output"]] = aid

    for aid, data in assignments.items():
        for inp in data["inputs"]:
            if inp in output_to_assignment:
                parent = output_to_assignment[inp]
                graph[parent].append(aid)
                indegree[aid] += 1

    return graph, indegree


def available_tasks(assignments, indegree, completed):
    return [
        a for a in assignments
        if indegree[a] == 0 and a not in completed
    ]