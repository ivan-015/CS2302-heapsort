# Ivan Vigliante
# CS2302 TR 10:20am-11:50am
# Lab 5A
# Professor Aguirre, Diego
# TA Saha Manoj
# Date of last modification: 11/27/2018
# Extra credit problem: Finds the nth number with a factor
# given by a specified list of integers.


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # List that will store all super ugly numbers
        super_ugly = [1]
        # Dictionary to keep track what index each prime number is at
        prime_indices = {}

        # Initialize dictionary entries to 0
        for num in primes:
            prime_indices[num] = 0

        # Compute super ugly numbers in order and stop when n is reached
        while len(super_ugly) < n:
            all_uglies = []
            # Compute and find the min of all super ugly numbers
            # at their respective indices
            for num in prime_indices:
                all_uglies.append(num * super_ugly[prime_indices[num]])
            min_ugly = min(all_uglies)

            # Match the min ugly to its position and add 1 to its index
            # in prime_indices
            for num in prime_indices:
                if min_ugly == num * super_ugly[prime_indices[num]]:
                    prime_indices[num] += 1
            # Add the super ugly number to the list
            super_ugly.append(min_ugly)

        # Return the last number(nth super ugly number))
        return super_ugly[len(super_ugly) - 1]

# Used to test solution class
cl = Solution()
n = 9
primes = [3,6,8]
print("The", n, "super ugly number is", cl.nthSuperUglyNumber(n,primes))