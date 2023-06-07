class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            if c & 1:
                count += 0 if ((a & 1) or (b & 1)) else 1
            else:
                count += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return count     
    

class TestClass:

    def test_one(self):
        input = [2,6,5] 
        test = Solution()
        assert test.minFlips(*input) == 3


    def test_two(self):
        input = [4,2,7]
        test = Solution()
        assert test.minFlips(*input) == 1
    

    def test_three(self):
        input = [1,2,3]
        test = Solution()
        assert test.minFlips(*input) == 0