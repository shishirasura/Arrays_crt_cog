'''Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]
Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 '''
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix=[0]
        for num in nums:
            self.prefix.append(self.prefix[-1]+num)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]
