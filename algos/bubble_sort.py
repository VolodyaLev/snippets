def bubble_sort(values):
    n = len(values)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
