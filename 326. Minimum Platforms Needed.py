def minimum_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    platforms = max_platforms=0
    i=j=0
    while i<len(arrivals):
        if arrivals[i]<departures[j]:
            platforms+=1
            max_platforms=max(max_platforms, platforms)
            i+=1
        else:
            platforms-=1
            j+=1
    return max_platforms

# Example Usage
arrivals = [900, 940, 950, 1100]
departures = [910, 1200, 1120, 1130]
print(minimum_platforms(arrivals, departures))  # Output: 3

