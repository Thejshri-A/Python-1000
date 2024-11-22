def targetSumOfElements(arr, target):
    
    suparr= []
    subarr=[]
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                if arr[i] + arr[j] == target:
                    subarr.append(i)
                    subarr.append(j)
                    if [i, j] and [j, i] not in suparr:
                        suparr.append(subarr)
                    subarr = []
    return suparr

arr = [2,7,11,15,2]
target = 9

print(targetSumOfElements(arr, target))
                    
    