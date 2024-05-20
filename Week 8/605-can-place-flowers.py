# Prompt: given an array of integers [flowerbed], containing the ints 0 and 1
# flowers can not be planted adjacent to each other
# 1 = full 0 = empty | and return n if flowers can be placed
#
# Todo: given an array of integers [flowerbed], containing the ints 0 and 1
# Todo: Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# Todo: and an integer n, return true if n new flowers can be planted in the flowerbed without
# Todo: violating the no-adjacent-flowers rule and false otherwise

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)
        # First, we need to store the length of any flowerbed, as well as count the number of flowers placed.
        for i in range(length):
            if flowerbed[i] == 0:
                empty_l = (i == 0 or flowerbed[i - 1] == 0)
                empty_r = (i == length - 1 or flowerbed[i + 1] == 0)
                # we need a way to iterate our range of values. our goal here is to check the adjacent pots,
                # or the values to the left and right of the list
                # knowing this, we then iterate through our flowerbeds,
                # using an if statement to iterate as a list with i, while our plots are empty.for this, we use [i] == 0
                # check the adjacent left or right flowerbeds (in the list, it would be the values before and after
                # we can do this by checking the values of the list, for each list value above and bellow current
                if empty_l or empty_r:
                    flowerbed[i] = 1
                    count += 1
                    # we now increase the count by one if the list is empty
                    if count >= n:
                        return True
        return count >= n


# Examples
class Solo:
    def __init__(self):
        self.solution = Solution()
        # Examples given:
        self.flowerbed1 = [1, 0, 0, 0, 1]
        self.n1 = 1
        print(self.solution.canPlaceFlowers(self.flowerbed1, self.n1))
        self.flowerbed2 = [1, 0, 0, 0, 1]
        self.n2 = 2
        print(self.solution.canPlaceFlowers(self.flowerbed2, self.n2))


if __name__ == '__main__':
    Solo()
