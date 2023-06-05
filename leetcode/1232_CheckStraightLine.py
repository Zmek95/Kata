from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) > 2:
            origin = coordinates[0]
            orig_gradient = None
            for point in coordinates[1:]:
                try:
                    gradient = (point[1] - origin[1]) / (point[0] - origin[0])
                except ZeroDivisionError:
                    gradient = float('inf')
                
                if orig_gradient == None:
                    orig_gradient = gradient
                elif orig_gradient == gradient:
                    pass
                else:
                    return False
        return True


class TestClass:

    def test_one(self):
        input = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]] 
        test = Solution()
        assert test.checkStraightLine(input) == True


    def test_two(self):
        input = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
        test = Solution()
        assert test.checkStraightLine(input) == False
    

    def test_three(self):
        input = [[1,2],[1,3],[1,4]]
        test = Solution()
        assert test.checkStraightLine(input) == True
