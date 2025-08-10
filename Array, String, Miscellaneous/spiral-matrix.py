# https://leetcode.com/problems/spiral-matrix/

'''RECURSION'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]):

        def recurse(matrix):
            if not matrix or not matrix[0]:
                return []

            top_row = [value for value in matrix[0]]

            right_col = []
            if len(matrix[0]) > 1:
                for i in range(1, len(matrix) - 1):
                    right_col.append(matrix[i][-1])
            else:
                for i in range(1, len(matrix) - 1):
                    right_col.append(matrix[i][0])

            bottom_row = []
            if len(matrix) > 1:
                for value in reversed(matrix[-1]):
                    bottom_row.append(value)

            left_col = []
            if len(matrix[0]) > 1:
                for i in range(len(matrix) - 2, 0, -1):
                    left_col.append(matrix[i][0])

            inner_matrix = []
            for i in range(1, len(matrix) - 1):
                if len(matrix[i]) > 2:
                    inner_matrix.append(matrix[i][1:-1])

            return top_row + right_col + bottom_row + left_col + recurse(inner_matrix)

        return recurse(matrix)


'''BRUTE-FORCE'''

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
