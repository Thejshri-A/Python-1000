def valid_subsequence_in_string(string, subseq):
    stringIndex, subseqIndex = 0,0
    
    while subseqIndex<len(subseq) and stringIndex<len(string):
        if subseq[subseqIndex] == string[stringIndex]:
            subseqIndex +=1 #Increasing Subsequence Index
        stringIndex +=1 #Increasing String Index
    return subseqIndex == len(subseq)

string = "abcdeninik"
subseq = "ain"
print(valid_subsequence_in_string(string, subseq))