def consecutive_sunny_days(weather):
    max_consec=0
    curr=0
    for i in range(len(weather)):
        while weather[i]==1:
            curr+=1
            i+=1
        max_consec=max(max_consec, curr)
        curr=0
    return max_consec

weather = [1, 1, 0, 1, 1, 1, 0]
print(consecutive_sunny_days(weather))