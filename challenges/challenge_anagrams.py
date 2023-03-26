# Fonte: Course

def merge_sort(entry):
    if len(entry) <= 1:
        return entry

    mid = len(entry) // 2
    left_side = merge_sort(entry[:mid])
    right_side = merge_sort(entry[mid:])

    return merge(left_side, right_side, list(entry))


def merge(left_side, right_side, array):
    i = j = 0

    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            array[i + j] = left_side[i]
            i += 1
        else:
            array[i + j] = right_side[j]
            j += 1

    for i in range(i, len(left_side)):
        array[i + j] = left_side[i]

    for j in range(j, len(right_side)):
        array[i + j] = right_side[j]

    return "".join(array)


def is_anagram(first_string, second_string):
    string1 = merge_sort(first_string.lower())
    string2 = merge_sort(second_string.lower())

    if string1 == string2 and string1 != '':
        return (string1, string2, True)
    else:
        return (string1, string2, False)
