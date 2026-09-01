class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if mp[temp]:
                return [mp[temp], i+1]
            mp[numbers[i]] = i+1 
        return []       
        