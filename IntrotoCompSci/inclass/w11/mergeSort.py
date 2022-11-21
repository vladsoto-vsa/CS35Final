"""
Merge sort is an example of a divide and conquer algorithm .
"""
def main():
    ls = [1, 4, 3, 5, 10, 7, 6, 9]
    print(ls)
    sorted_ls = mergeSort(ls)
    print(sorted_ls)
def mergeSort(ls):
    """
    Inputs: An unsorted list
    Return: A new list with the items from the original list now in sorted
    order
    """
    print("mergeSort: ", ls)
    if len(ls) <= 1:
        return ls

    else:
        midpoint = len(ls)//2
        sorted_half1 = mergeSort(ls[:midpoint])
        sorted_half2 = mergeSort(ls[midpoint:])
        combined = merge(sorted_half1, sorted_half2)
        return combined
def merge(ls1, ls2):
    """
    Inputs: Two sorted lists ls1 and ls2
    Returns: A new combined sorted list made fro the elements of ls1 and ls2

    suppose ls1 = [1, 4, 6, 7] and ls2 = [2, 5, 10, 12]
    index1 = 0, 1, 1, 2, 2, 3, 4
    index2 = 0, 0, 1, 1, 2, 2, 2,
    compare elements in each list using index1 for ls1 and index2 for ls2
    combined = [1,2,4,5, 6, 7, 10, 12]
    """
    print("merge:", ls1, ls2)
    index1 = 0
    index2 = 0
    combined = []
    while index1 < len(ls1) and index2 < len(ls2):
        if ls1[index1] <= ls2[index2]:
            combined.append(ls[index1])
            index1 += 1

        else:
            combined.append(ls2[index2])
            index2 += 1
    if index1 < len(ls1):
        combined = combined + ls1[index1:]
    else:
        combined = combined + ls2[index2:]
    print("done", combined)
    return combined
