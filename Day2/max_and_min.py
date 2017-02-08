def find_max_min(num):
    numbers = sorted(num)
    max_min = []
    if numbers[1:] == numbers[:-1]:
        max_min.append(len(numbers))
    else:
        min_num = min(numbers)
        max_num = max(numbers)
        max_min.append(min_num)
        max_min.append(max_num)
    return max_min