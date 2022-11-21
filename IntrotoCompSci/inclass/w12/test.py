def main():
    list = [17, 4, 19, 3, 11, 8]
    answer = selectionSort(list)



def selectionSort(ls):
    for i in range(len(ls)):
        indexOfMin = i # location of min item in remaining list
        for j in range(i+1, len(ls)):
            if ls[j] < ls[indexOfMin]:
                indexOfMin = j
        s = ls[indexOfMin]
        ls[indexOfMin] = ls[i]
        ls[i] = s
        print(ls)

    return ls

main()
