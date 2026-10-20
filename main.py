m = 100_000 + 1
divisors = [[1] for _ in range(m)]
for i in range(2, m):
    for j in range(i, m, i):
        divisors[j].append(i)

def is_sortable_by_cycling_subarrays(nums: list[int], k: int) -> bool:
    if k == 1:
        return nums == list(sorted(nums))
    maximum = 0
    local_maximum = maximum
    for subarray in batched(nums, k):
        found_decrease = False
        for a, b in pairwise(chain(subarray, (subarray[0],))):
            if a < maximum:
                return False
            if a > local_maximum:
                local_maximum = a
            if a > b:
                if found_decrease:
                    return False
                found_decrease = True
                local_maximum = a
        maximum = local_maximum
    return True

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        return sum(k for k in divisors[len(nums)] if is_sortable_by_cycling_subarrays(nums, k))
            
