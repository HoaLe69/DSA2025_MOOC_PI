"""
A restaurant is visited by n customers during a given day, and you know the arrival
and departure time of each customer. If a customer departs at the same moment as another
arrives, they are both considered to be in the restaurant at that moment. Your task is to find
out the highest number of customers that are in the restaurant at the same time.

Consider the following example case:

Customer	Arrival time	Departure time
#1	        6	                8
#2	        3	                7
#3	        6	                9
#4	        1	                5
#5	        2	                8

Here the highest number of customers is 4: the customers #1,#2,#4 and #5 are all
in the restaurant during the time period 6-7.
"""

arrival_time = [6, 3, 6, 1, 2]
departure_time = [8, 7, 9, 5, 8]


# Solution : O(n log n) process events in order of time.
def max_customers(arrival, departure):
    events = []
    for time in arrival:
        events.append((time, 1))
    for time in departure:
        events.append((time, 2))
    events.sort()
    counter = 0
    result = 0

    for event in events:
        if event[1] == 1:
            counter += 1
        if event[1] == 2:
            counter -= 1
        result = max(result, counter)
    return result


print(max_customers(arrival_time, departure_time))
