def compute_operations(n):

    steps_list = [[], [1], ]

    for num in range(2, n + 1):

        least_steps = []

        if num - 1 > 0:
            steps = steps_list[num - 1].copy()
            steps.append(num)
            least_steps[:] = steps

        if num % 2 == 0:
            new_steps = steps_list[num // 2].copy()
            new_steps.append(num)
            if len(new_steps) < len(least_steps):
                least_steps[:] = new_steps

        if num % 3 == 0:
            new_steps = steps_list[num // 3].copy()
            new_steps.append(num)
            if len(new_steps) < len(least_steps):
                least_steps[:] = new_steps

        steps_list.append(least_steps)

    return steps_list[n]

print(compute_operations(1))
