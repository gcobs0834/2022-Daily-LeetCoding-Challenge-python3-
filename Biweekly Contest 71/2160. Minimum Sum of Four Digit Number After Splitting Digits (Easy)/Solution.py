    def minimumSum(self, num: int) -> int:
        nums = [int(c) for c in str(num)]
        nums.sort()
        return nums[0] * 10 + nums[1] * 10 + nums[2] + nums[3]
