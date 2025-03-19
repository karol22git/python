
result = {tuple([])}

def Subsets(arr: list) -> None:
    if len(arr) == 0:
        return
    result.add(tuple(arr))
    for i in range(0, len(arr)):
        tmp = arr.copy()
        tmp.pop(i)
        Subsets(tmp)

l = [1,2,3,4,5]

Subsets(l)

print(len(result))