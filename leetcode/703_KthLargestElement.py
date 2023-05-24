import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]) -> None:
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


class TestClass:

    def base_test(self, input, output):
        obj = KthLargest(input[0][0], input[0][1])
        assert obj.k == input[0][0]
        assert obj.nums == input[0][1]
        for idx, num in enumerate(input[1:]):
            kth_value = obj.add(num[0])
            assert kth_value == output[idx]  


    def test_one(self):
        input =[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
        output = [4,5,5,8,8] 
        test = TestClass()
        test.base_test(input,output)


    def test_two(self):
        input =[[3,[4,5,8,2]],[3],[5],[10],[9],[4],[0],[100]]
        output = [4,5,5,8,8,8,9] 
        test = TestClass()
        test.base_test(input,output)
