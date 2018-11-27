# Ivan Vigliante
# CS2302 TR 10:20am-11:50am
# Lab 5A
# Professor Aguirre, Diego
# TA Saha Manoj
# Date of last modification: 11/27/2018
# Extra credit problem that finds the nth ugly number.
# The nth ugly number is defined by: positive numbers
# whose prime factors only include 2, 3, 5.


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initial list with only 1
        ugly_list = [1]
        # Keep track of the index where each multiplier is
        index_2 = 0
        index_3 = 0
        index_5 = 0
        while len(ugly_list) < n:
            next_ugly = min(ugly_list[index_2] * 2, ugly_list[index_3] * 3, ugly_list[index_5] * 5)
            # Move the index of the min, since we calculated the number for the previous
            if next_ugly == ugly_list[index_2] * 2:
                index_2 += 1
            if next_ugly == ugly_list[index_3] * 3:
                index_3 += 1
            if next_ugly == ugly_list[index_5] * 5:
                index_5 += 1
            ugly_list.append(next_ugly)
        return ugly_list[len(ugly_list) - 1]

cl = Solution()
n = 8
print("The", n, "ugly number is", cl.nthUglyNumber(n))