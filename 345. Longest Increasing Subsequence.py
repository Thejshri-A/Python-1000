def lis(arr):
    dp=[1]*(len(arr))
    n=len(arr)
    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i], dp[j]+1)
    return max(dp, default=0)

arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis(arr))