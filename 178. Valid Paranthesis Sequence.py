def valid_paranthesis_seq(seq):
    temp_seq=[]
    for i in range(len(seq)):
        if seq[i]=="(":
            temp_seq.append(seq[i])
        elif seq[i]==")" and temp_seq:
            temp_seq.pop()
        else:
            return False
        
    if len(temp_seq) != 0:
        return False
    else:
        return True
    
seq="(()(()))()"
print(valid_paranthesis_seq(seq))