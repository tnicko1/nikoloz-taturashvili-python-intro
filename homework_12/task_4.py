"""
Write a function that takes two sorted lists and returns a new list containing the elements from both lists in sorted order.
From the main function, test your function for different inputs.
Do not use the sort and sorted functions.
Try to merge the two lists so that the sorting is not broken.
"""

def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

def main():
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
    print(merge_sorted_lists([1, 2, 3], [2, 3, 4]))
    print(merge_sorted_lists([], [1, 2, 3]))
    print(merge_sorted_lists([1, 2, 3], []))
    print(merge_sorted_lists([], []))
    print(merge_sorted_lists([1, 2, 3, 4], [5, 6]))
    print(merge_sorted_lists([3, 4, 5], [5, 6, 7, 8]))
    print(merge_sorted_lists([-3, -1, 1], [-2, 0, 2]))

if __name__ == '__main__':
    main()