# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)

        original = []
        for row in matrix:
            original.append(row[:])

        for i in range(length):
            for j in range(length):
                matrix[j][length - 1 - i] = original[i][j]
