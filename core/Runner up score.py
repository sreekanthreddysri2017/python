if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = list(arr)
    arr2 = [i for i in arr1 if i!=max(arr1)]
    print(max(arr2))