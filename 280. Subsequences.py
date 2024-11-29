def subsequence_of_arr(arr):
    subseq=[]
    def dfs(path, index):
        if index==len(arr):
            if path:
                subseq.append(path)
            return
        dfs(path+arr[index], index+1)
        dfs(path, index+1)
    dfs("", 0)
    return subseq

# Example Usage
print(subsequence_of_arr("abc"))