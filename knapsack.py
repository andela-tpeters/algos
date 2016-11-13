def knapsack_01(values, weights, total):
    total_items = len(weights)

    rows = total_items + 1
    cols = total + 1

    T = [[0 for _ in range(cols)] for _ in range(rows)]
    # print(T)
    for i in range(1, rows):
        for j in range(1, cols):
            if j < weights[i - 1]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], values[i - 1] + T[i - 1][j - weights[i - 1]])

    print(T)
    return T[rows - 1][cols -1]


print(knapsack_01([3,1,3], [2,2,1], 4))