# Ivan Vigliante
# CS2302 TR 10:20am-11:50am
# Lab 5A
# Professor Aguirre, Diego
# TA Saha Manoj
# Date of last modification: 11/27/2018
# Extra credit problem: Finds the kth largest element in a list
# Assumes k is a number less than or equal to the length of the list
# and that the list is populated


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sort the list
        self.quicksort(nums, 0, len(nums) - 1)

        # Return the k largest element
        return nums[len(nums) - k]


    def quicksort(self, nums_list, start, end):
        # If end crosses or is equal to start, list is sorted
        if end <= start:
            return

        # Split the list into low and high partitions
        index_high = self.split_list(nums_list, start, end)

        # Recursively sort the two resulting lists
        self.quicksort(nums_list, start, index_high)
        self.quicksort(nums_list, index_high + 1, end)


    def split_list(self, nums_list, start, end):
        low = start
        high = end
        # Get midpoint and pivot
        mid = (high - low) // 2 + low
        pivot = nums_list[mid]

        while True:
            # While element in list is less than pivot,
            # move right in list
            while nums_list[low] < pivot:
                low += 1
            # While element in list is greater than pivot,
            # move left in the list
            while nums_list[high] > pivot:
                high -= 1

            # If low is greater than or equal to high,
            # splitting is finished
            if low >= high:
                break
            # Otherwise, swap the two elements where we stopped
            # and keep going
            temp = nums_list[low]
            nums_list[low] = nums_list[high]
            nums_list[high] = temp

            # Move high and low pointers
            low += 1
            high -= 1

        # Returns the last index of the low partition(where high stopped)
        return high


# Used to test the functions
cl = Solution()
test_list = [3, 6, 8, 0, 1, 5, 8, 25, 10, 9, 20, 27, 2]
k = 5
kth_largest = cl.findKthLargest(test_list, k)
print("The", k, "largest number is",kth_largest)