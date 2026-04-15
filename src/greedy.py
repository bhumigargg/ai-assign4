from collections import Counter
from .utils import build_dependency_graph, available_tasks


def greedy_food_cost(assignments, costs, g):

    graph, indegree = build_dependency_graph(assignments)

    completed = set()
    days = []
    total_cost = 0

    while len(completed) < len(assignments):

        avail = available_tasks(assignments, indegree, completed)

        avail.sort(key=lambda x: costs[assignments[x]["food"]])

        today = avail[:g]

        menu = Counter([assignments[t]["food"] for t in today])

        cost = sum(menu[f] * costs[f] for f in menu)

        total_cost += cost
        days.append((today, menu, cost))

        for t in today:
            completed.add(t)

            for nxt in graph[t]:
                indegree[nxt] -= 1

    return days, total_cost



def greedy_food_frequency(assignments, costs, g):

    graph, indegree = build_dependency_graph(assignments)

    completed = set()
    days = []
    total_cost = 0

    food_freq = Counter(a["food"] for a in assignments.values())

    while len(completed) < len(assignments):

        avail = available_tasks(assignments, indegree, completed)

        avail.sort(key=lambda x: -food_freq[assignments[x]["food"]])

        today = avail[:g]

        menu = Counter([assignments[t]["food"] for t in today])

        cost = sum(menu[f] * costs[f] for f in menu)

        total_cost += cost
        days.append((today, menu, cost))

        for t in today:
            completed.add(t)

            for nxt in graph[t]:
                indegree[nxt] -= 1

    return days, total_cost