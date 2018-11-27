# Ivan Vigliante
# CS2302 TR 10:20am-11:50am
# Lab 5A
# Professor Aguirre, Diego
# TA Saha Manoj
# Date of last modification: 11/27/2018
# The purpose of this program is to implement a min heap
# class that correctly inserts and extracts elements in
# the heap. Then, the program uses this heap class to implement
# heap sort and print the sorted array.


class Heap:

    def __init__(self):
        self.heap_array = []

    def insert(self, elem):
        self.heap_array.append(elem)

        i = len(self.heap_array) - 1
        while i > 0:
            # If element inserted is less than its parent, swap
            if self.heap_array[i] < self.heap_array[(i-1)//2]:
                temp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[(i-1)//2]
                self.heap_array[(i-1)//2] = temp
                i = (i-1)//2
            # Otherwise, no need to swap
            else:
                break

    # This function extracts the min element from a heap and
    # ensures the heap properties are preserved
    def extract_min(self):
        if self.is_empty():
            return None

        min_elem = self.heap_array[0]
        # Pop the last element of the list
        new_first = self.heap_array.pop()
        # If heap contains elements after extracting, check heap for violations
        if len(self.heap_array) > 0:
            # Make the last element of the list the head
            self.heap_array[0] = new_first
            i = 0
            while i < len(self.heap_array):
                c_index = 2*i+1
                rc_index = 2*i+2
                min_index = i  # Variable to store the min value to swap
                # check left and right children of current node (if they exist)
                while c_index < len(self.heap_array) and c_index <= rc_index:
                    # If the current min value is greater than the child,
                    # make the index of the child the new min.
                    if self.heap_array[min_index] > self.heap_array[c_index]:
                        min_index = c_index
                    c_index += 1
                # If all three values are the same, or the node has no children, no need to swap
                if i == min_index:
                    break
                # Otherwise, swap the current node with the min
                temp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[min_index]
                self.heap_array[min_index] = temp

                # Continue swapping if necessary
                i = min_index

        # Return the min element after fixing heap
        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0


# This function receives a min-heap and returns a sorted array
def heapsort(heap):
    result = []
    for i in range(len(heap.heap_array)):
        result.append(heap.extract_min())
    return result


# This function creates and returns a heap reading numbers from a file
def create_heap(filename):
    file = open(filename, "r")
    heap = Heap()
    numbers = file.readline().split(",")
    for number in numbers:
        heap.insert(int(number))
    return heap


# Function that allows user to provide file to test the heapsort function.
def test():
    while True:
        try:
            filename = input("Enter the path to the txt file that contains the numbers separated by commas (press RETURN for default file or \"q\" to quit):\n")
            # If user pressed RETURN, use default file
            if filename == "":
                filename = "numbers.txt"
            elif filename.lower() == "q":
                return
            # Create heap with specified or default file
            heap = create_heap(filename)
            # Sort array using heapsort
            sorted = heapsort(heap)
            print("Sorted array using heapsort:")
            # Print the sorted array, 40 numbers per line max
            for i in range(len(sorted)):
                if i%40 == 0:
                    print()
                print(str(sorted[i]), end="")
                if i != len(sorted)-1:
                    print(", ", end="")
            print()
            return
        except FileNotFoundError:
            print("File was not found. Please try again.")
        except ValueError:
            print("ValueError: Please verify that the file contains only integers separated by commas.")
        except Exception as ee:
            print(ee)

test()
