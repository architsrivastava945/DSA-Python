# Problem:
# Given a schedule of arrivals and departures for trains at a railway station, find the minimum number of platforms required so that no train has to wait.

# Example:

# Arrivals = [9:00, 9:40, 9:50, 11:00, 15:00, 18:00]

# Departures = [9:10, 12:00, 11:20, 11:30, 19:00, 20:00]

# Output: 3 platforms.

def Abigger(a, b):
    [Ahour, Aminute] = a.split(":")
    [Bhour, Bminute] = b.split(":")
    if Ahour > Bhour:
        return True
    elif Ahour < Bhour:
        return False
    else:
        if Aminute >= Bminute:
            return True
        else:
            return False

def platformCounter(arrival:List, departures:List) -> Int:
    n = len(arrival)

    # sorting
    for i in range(n):
        big = 0
        for j in range(n-i):
            if Abigger(arrival[j], arrival[big]):
                big = j
        if big:
            arrival[big], arrival[n-i-1] = arrival[n-i-1], arrival[big]
            departures[big], departures[n-i-1] = departures[n-i-1], departures[big]

    count = 1
    maxDepart = "00:00"
    for i in range(n):
        if Abigger(maxDepart, arrival[i]):
            count += 1
        else:
            count -= 1
        if Abigger(departures[i], maxDepart):
            maxDepart = departures[i]

        pass

def counterPlatforms(arrival, departure):
    n = len(arrival)
    for i in range(n):
        bigArrival = 0
        bigDepart = 0
        for j in range(n-i):
            if Abigger(arrival[j], arrival[bigArrival]):
                bigArrival = j
            if Abigger(departure[j], departure[bigDepart]):
                bigDepart = j
        if bigArrival:
            arrival[n-i-1], arrival[bigArrival] = arrival[bigArrival], arrival[n-i-1]
        if bigDepart:
            departure[n-i-1], departure[bigDepart] = departure[bigDepart], departure[n-i-1]

    maxPlateform = 1
    count = 1
    i, j = 1, 0
    while (i < n or j < n):
        if Abigger(arrival[i], departure[j]):
            count -= 1
        else :
            count += 1
        maxPlateform = max(maxPlateform, count)
    return maxPlateform