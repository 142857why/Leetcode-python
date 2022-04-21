from typing import List


class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]],
                    limit: int) -> int:
        max_delicious_value = -1
        n = len(cookbooks)
        nums = [x for x in range(n)]

        def subsets(nums):
            res = [[]]
            for num in nums:
                res += [i + [num] for i in res]
            return res

        all_possibilities = subsets(nums)
        for p in all_possibilities:
            m = materials.copy()
            current_delicious = 0
            current_energy = 0
            flag = True
            for index in p:
                for i, usage in enumerate(cookbooks[index]):
                    m[i] -= usage
                    if m[i] < 0:
                        flag = False
                        break
                current_energy += attribute[index][1]
                current_delicious += attribute[index][0]

            if flag:
                if current_energy >= limit:
                    max_delicious_value = max(max_delicious_value, current_delicious)

        return max_delicious_value


if __name__ == '__main__':
    sol = Solution()
    materials = [3,2,4,1,2]
    cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]
    attribute = [[3,2],[2,4],[7,6]]
    limit = 5
    print(sol.perfectMenu(materials, cookbooks, attribute, limit))
