"""
How many ways can you place n queens on an nxn chess board so that no two queens
attack each other ?
Two queens attack each other if they are on the same row , column or diagonal.

"""


def count_queens(n):
    anwser = []
    count(n, 0, [], anwser)
    print(anwser)


def output_processor(coordinate, n):
    output = ""
    for i in range(n):
        if i == coordinate[1]:
            output += "Q"
        else:
            output += "."
    return output


def count(n, row, queens, anwser):
    if row == n:
        ans = []
        for queen in queens:
            ans.append(output_processor(queen, n))
        anwser.append(ans)
        return 1
    result = 0
    for col in range(n):
        attacks = []
        for queen in queens:
            attacks.append(attack(queen, (row, col)))
        if not any(attacks):
            result += count(n, row + 1, queens + [(row, col)], anwser)
    return result


def attack(queen1, queen2):
    # check the same row or col
    if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
        return True
    # check the same diagonal
    if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
        return True
    return False


count_queens(8)
