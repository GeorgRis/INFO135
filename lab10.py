#1
def detailed_knap_sack(values, weigths, capacity):
    grid = [[(0, False) for x in range(capacity+1)]for x in range(len(weigths)+1)]

    for i in range(1, len(weigths)+1):
        for w in range(1, capacity+1):
            if weigths[i-1] <= w:
                include = values[i-1] + grid[i-1][w-weights[i-1]][0]
                exclude = grid[i-1][w][0]
                if include > exclude:
                    grid[i][w] = (include, True)
                else:
                    grid[i][w] = (exclude, False)
            else: grid[i][w] = grid[i-1][w]

    items_included = []
    w = capacity
    for i in range(len(weights), 0, -1):
        if grid[i][w][1]:  # If the item was included
            items_included.append(weights[i - 1])
            w -= weights[i - 1]

    return grid[len(weights)][capacity][0], items_included



values = [120, 200, 150, 350, 100, 90]
weights = [15, 20, 40, 50, 20, 10]
capacity = 100

value, used_w=detailed_knap_sack(values, weights, capacity)
print(f"{value}$ {used_w}")

#2

