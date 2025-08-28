#!/bin/python3

"""
Matrix Layer Rotation - HackerRank Problem

You are given a 2D matrix of dimension M x N and a positive integer R. 
You have to rotate the matrix R times and print the resultant matrix. 
Rotation should be in anti-clockwise direction.

It is guaranteed that the minimum of M and N will be even.

As an example rotate the Start matrix by 2:

    Start         First           Second
     1 2 3 4       2  3  4  5      3  4  5  6
    12 1 2 5  ->   1  2  3  6 ->   2  3  4  7
    11 4 3 6      12  1  4  7      1  2  1  8
    10 9 8 7      11 10  9  8     12 11 10  9

Function Description

Complete the matrixRotation function in the editor below.

matrixRotation has the following parameter(s):

int matrix[m][n]: a 2D array of integers
int r: the rotation factor

Prints

It should print the resultant 2D integer array and return nothing. 
Print each row on a separate line as space-separated integers.

Input Format

The first line contains three space separated integers, M, N, and R, 
the number of rows and columns in matrix, and the required rotation.
The next M lines contain N space-separated integers representing the elements of a row of matrix.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    
    result = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    
    while left < right - 1 and top < bottom - 1:
        
        elements = []
        
        # top row
        for col in range(left, right):
            elements.append(matrix[top][col])
        
        # right col
        for row in range(top + 1, bottom - 1):
            elements.append(matrix[row][right - 1])
        
        # bottom row
        for col in reversed(range(left, right)):
            elements.append(matrix[bottom - 1][col])
        
        # left col
        for row in reversed(range(top + 1, bottom - 1)):
            elements.append(matrix[row][left])
        
        rotation = r % len(elements)
        rotated = elements[rotation: ] + elements[: rotation]
        
        currentIndex = 0
        
        # top row assignment
        for col in range(left, right):
            result[top][col] = rotated[currentIndex]
            currentIndex += 1
        
        # right col assignment
        for row in range(top + 1, bottom - 1):
            result[row][right - 1] = rotated[currentIndex]
            currentIndex += 1
        
        # bottom row assignment
        for col in reversed(range(left, right)):
            result[bottom - 1][col] = rotated[currentIndex]
            currentIndex += 1
        
        # left col assignment
        for row in reversed(range(top + 1, bottom - 1)):
            result[row][left] = rotated[currentIndex]
            currentIndex += 1
        
        left += 1
        right -= 1
        top += 1
        bottom -= 1
        
    for row in result:
        print(*row)


def test_matrix_rotation():
    """Test cases for matrixRotation function"""
    print("Testing Matrix Layer Rotation...")

    # Test 1: 4x4 matrix with 2 rotations (from problem example)
    matrix1 = [
        [1, 2, 3, 4],
        [12, 1, 2, 5],
        [11, 4, 3, 6],
        [10, 9, 8, 7]
    ]
    r1 = 2
    print(f"Test 1: 4x4 matrix, {r1} rotations")
    print("Input matrix:")
    for row in matrix1:
        print(row)
    print("Output after rotation:")
    matrixRotation(matrix1, r1)
    print()

    # Test 2: 3x3 matrix with 1 rotation
    matrix2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    r2 = 1
    print(f"Test 2: 3x3 matrix, {r2} rotation")
    print("Input matrix:")
    for row in matrix2:
        print(row)
    print("Output after rotation:")
    matrixRotation(matrix2, r2)
    print()

    # Test 3: 2x2 matrix with 3 rotations
    matrix3 = [
        [1, 2],
        [3, 4]
    ]
    r3 = 3
    print(f"Test 3: 2x2 matrix, {r3} rotations")
    print("Input matrix:")
    for row in matrix3:
        print(row)
    print("Output after rotation:")
    matrixRotation(matrix3, r3)
    print()

    # Test 4: Single element matrix
    matrix4 = [[42]]
    r4 = 5
    print(f"Test 4: 1x1 matrix, {r4} rotations")
    print("Input matrix:")
    for row in matrix4:
        print(row)
    print("Output after rotation:")
    matrixRotation(matrix4, r4)
    print()

    # Test 5: Large rotation count (should handle modulo)
    matrix5 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    r5 = 9  # Should be equivalent to 9 % 8 = 1 rotation
    print(f"Test 5: 3x3 matrix, {r5} rotations (tests modulo)")
    print("Input matrix:")
    for row in matrix5:
        print(row)
    print("Output after rotation:")
    matrixRotation(matrix5, r5)
    print()


if __name__ == '__main__':
    # For local testing - run the test cases
    test_matrix_rotation()

    # Uncomment below for HackerRank submission
    # first_multiple_input = input().rstrip().split()
    # m = int(first_multiple_input[0])
    # n = int(first_multiple_input[1])
    # r = int(first_multiple_input[2])
    # matrix = []
    # for _ in range(m):
    #     matrix.append(list(map(int, input().rstrip().split())))
    # matrixRotation(matrix, r)
