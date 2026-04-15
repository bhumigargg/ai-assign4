import heapq
from collections import Counter
from .utils import build_dependency_graph, available_tasks


class State:

    def __init__(self, completed, cost, days):
        self.completed = completed
        self.cost = cost
        self.days = days

    def __lt__(self, other):
        return self.cost < other.cost



def heuristic(assignments, completed, costs):

    remaining = [
        assignments[a]["food"]
        for a in assignments
        if a not in completed
    ]

    return sum(costs[f] for f in remaining)



def astar_schedule(assignments, costs, g):

    graph, indegree_init = build_dependency_graph(assignments)

    start = State(set(), 0, [])

    pq = []
    heapq.heappush(pq, (0, start))

    explored = 0

    while pq:

        _, state = heapq.heappop(pq)
        explored += 1

        if len(state.completed) == len(assignments):
            return state.days, state.cost, explored

        indegree = indegree_init.copy()

        for c in state.completed:
            for nxt in graph[c]:
                indegree[nxt] -= 1

        avail = available_tasks(assignments, indegree, state.completed)

        for i in range(1, min(g, len(avail)) + 1):

            today = avail[:i]

            menu = Counter(assignments[t]["food"] for t in today)

            day_cost = sum(menu[f] * costs[f] for f in menu)

            new_completed = state.completed | set(today)

            new_days = state.days + [(today, menu, day_cost)]

            g_cost = state.cost + day_cost

            f_cost = g_cost + heuristic(assignments, new_completed, costs)

            heapq.heappush(
                pq,
                (f_cost, State(new_completed, g_cost, new_days))
            )