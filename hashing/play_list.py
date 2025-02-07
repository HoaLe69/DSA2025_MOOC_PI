"""
You are given a play list, where each song is represented by an integer.
Your task to find out how long is the longest part of the play list that
contains no song twice.

Ex : [1,2,1,3,5,4,3,1] -> the desired answer is 5, which is length of the play list part [2,1,3,5,4]
"""

songs = [1, 2, 1, 3, 5, 4, 3, 1]


# Best solution : O(n)
def max_length(songs):
    start = 0
    length = 0  # output

    pos = {}

    for i, song in enumerate(songs):
        if song in pos:
            start = max(start, pos[song] + 1)
        length = max(length, i - start + 1)
        pos[song] = i

    return length


print(max_length(songs))
