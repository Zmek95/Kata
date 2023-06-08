from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_count = 0
        row_len = len(grid[0])
        for row in grid:
            left, right = 0, row_len - 1
            while left <= right:
                mid = (right + left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            neg_count += row_len - left
        return neg_count
    

class TestClass:

    def test_one(self):
        input = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] 
        test = Solution()
        assert test.countNegatives(input) == 8


    def test_two(self):
        input = [[3,2],[1,0]]
        test = Solution()
        assert test.countNegatives(input) == 0
