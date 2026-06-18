"""
Problem: Valid Sudoku

LeetCode: 36
Difficulty: Medium

Pattern:
Hash Set Validation

Approach:
1. Use three hash maps of sets:
   - rows[r] stores values seen in row r
   - cols[c] stores values seen in column c
   - boxes[(r//3, c//3)] stores values seen in a 3x3 box
2. Traverse the board.
3. Skip empty cells (".").
4. If a value already exists in its row, column, or box,
   the board is invalid.
5. Otherwise, add the value to all three sets.

Time Complexity:
O(81) = O(1)

Space Complexity:
O(81) = O(1)

Key Learning:
Use multiple hash sets to efficiently enforce
independent constraints on the same data.
"""

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                box_index = (r // 3, c // 3)

                if (
                    val in rows[r]
                    or val in cols[c]
                    or val in boxes[box_index]
                ):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True
