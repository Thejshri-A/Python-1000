def maxDist(seats):
    maximum_distance = 0
    last_person = -1
    
    for i in range(len(seats)):
        if seats[i]==1:
            if last_person == -1:
                maximum_distance = i
            else:
                maximum_distance = max(maximum_distance, (i-last_person)//2)
            last_person = i
        
    maximum_distance = max(maximum_distance, (len(seats) - last_person - 1))
    return maximum_distance


# Example
seats = [1, 0, 0, 0, 1, 0, 1]
print(maxDist(seats))  # Output: 2                

