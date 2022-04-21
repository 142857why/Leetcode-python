import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqHeap = []
        heapq.heapify(freqHeap)
        count = Counter(nums)

        for key, value in count.items():
            if len(freqHeap) >= k:
                if value > freqHeap[0][0]:
                    heapq.heapreplace(freqHeap, (value, key))
            else:
                heapq.heappush(freqHeap, (value, key))
        return [item[1] for item in freqHeap]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(sol.topKFrequent(nums, k=2))

