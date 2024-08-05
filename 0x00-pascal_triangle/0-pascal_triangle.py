#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    result = []
    prev_result = []
    for i in range(n):
        curr_result = []

        if i == 0:
            prev_result = [1, 1]
            print([1])
            continue

        for j in range(i + 1):
            if j == (0) or j == (i):
                curr_result.append(1)
            else:
                curr_result.append(prev_result[j-1] + prev_result[j])

        result.append(curr_result)

        prev_result = curr_result

    return result
