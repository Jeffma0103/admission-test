def find_max(numbers):
    max_num = numbers[0]
    for i in range(len(numbers)):
        if max_num < numbers[i]:
            max_num = numbers[i]
    return max_num

def find_position(numbers, target):
    target_num = -1
    for i in range(len(numbers)):
        if numbers[i] == target :
            return i
        else:
            continue
    return target_num