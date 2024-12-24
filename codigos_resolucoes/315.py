from bisect import bisect_left

class Solution:
    def countSmaller(self, nums):
        sorted_nums = sorted(set(nums))
        rank = {num: i + 1 for i, num in enumerate(sorted_nums)}

        fenwick_tree = [0] * (len(sorted_nums) + 1)

        def update(index, value):
            while index < len(fenwick_tree):
                fenwick_tree[index] += value
                index += index & -index

        def query(index):
            sum_ = 0
            while index > 0:
                sum_ += fenwick_tree[index]
                index -= index & -index
            return sum_

        counts = []
        for num in reversed(nums):
            rank_index = rank[num]
            counts.append(query(rank_index - 1))
            update(rank_index, 1)

        return counts[::-1]

solution = Solution()