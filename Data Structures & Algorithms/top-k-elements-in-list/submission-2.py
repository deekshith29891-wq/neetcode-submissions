class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ls = [x for x, _ in Counter(nums).most_common(k)]
        return sorted(ls, reverse = False)
