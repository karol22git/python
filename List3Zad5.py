
result = []
def Permutation(k: int, arr: list) -> None:
    if k == 0:
        return result.append(arr)
    else:
        Permutation(k-1,arr.copy())
        for i in range(0,k):
            if k%2 == 0:
                tmp = arr[i]
                arr[i] = arr[k-1]
                arr[k-1] = tmp
            else:
                tmp = arr[0]
                arr[0] = arr[k-1]
                arr[k-1] = tmp
            Permutation(k-1, arr.copy())
l = [1,2,3,4,5,6]
Permutation(5,l)
print(len(result))