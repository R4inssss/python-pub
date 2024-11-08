
nums = [2,7,11,15]
target = 9

class solutions:
    def twoSums(self,nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                print(n)
                if nums[i] + nums[j] == target:
                    print(i, j)
                    return[i,j]
        print(n)
        return []


nums = [2,7,11,15], target = 9
