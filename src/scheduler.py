def print_schedule(strategy, days, total_cost):

    print("\nStrategy:", strategy)

    for i, (tasks, menu, cost) in enumerate(days):

        menu_str = ", ".join(
            f"{v}-{k}" for k, v in menu.items()
        )

        print(
            f"Day-{i+1}: "
            + ", ".join(f"A{t}" for t in tasks)
            + f"   Menu: {menu_str}   Cost: {cost}"
        )

    print("Total Days:", len(days),
          " Total Cost:", total_cost)