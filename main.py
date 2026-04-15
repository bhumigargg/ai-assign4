from src.parser import parse_input
from src.greedy import greedy_food_cost, greedy_food_frequency
from src.astar import astar_schedule
from src.scheduler import print_schedule


def run(file):

    costs, g, inputs, outputs, assignments = parse_input(file)

    days1, cost1 = greedy_food_cost(assignments, costs, g)

    print_schedule(
        "Greedy by Food Cost",
        days1,
        cost1
    )


    days2, cost2 = greedy_food_frequency(assignments, costs, g)

    print_schedule(
        "Greedy by Food Frequency",
        days2,
        cost2
    )


    days3, cost3, explored = astar_schedule(
        assignments,
        costs,
        g
    )

    print_schedule(
        "A* Optimal",
        days3,
        cost3
    )

    print("States Explored:", explored)



if __name__ == "__main__":

    for f in [
        "input/test1.txt",
        "input/test2.txt",
        "input/test3.txt"
    ]:
        print("\n====================")
        print("Running:", f)
        run(f)