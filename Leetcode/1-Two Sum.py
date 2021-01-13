def twoSum(self, nums: List[int], target: int) -> List[int]:
    res_index = []
    for i in range(len(nums)):
      p = target - nums[i]
      if p in (nums[:i]+nums[i+1:]):
          res_index.append(i)
          res_index.append((nums[:i]+nums[i+1:]).index(p)+1)
          break
    return res_index
