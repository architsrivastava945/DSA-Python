def knapsack(idx, W):
    if idx > len(value) or W <= 0:
        return 0
    return max(value[idx] + knapsack(idx+1, W - weight[idx]), knapsack(idx+1, W))