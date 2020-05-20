class Solution:    
    def merge_sort(self, array, left_index, right_index):
        if left_index >= right_index:
            return
        
        middle = (left_index + right_index)//2 #// == floor division (rounds the result down to the nearest whole number)

        self.merge_sort(array, left_index, middle) # Subdivide left array
        self.merge_sort(array, middle + 1, right_index) # Subdivide right array

        # Once all divisions have occured, begin sorting process
        self.merge(array, left_index, right_index, middle)


    def merge(self, array, left_index, right_index, middle):
        # Make copies of both arrays we're trying to merge - the second parameter is non-inclusive, so we have to increase by 1
        left_copy = array[left_index:middle + 1]
        right_copy = array[middle+1:right_index+1]

        # Initial values for variables that we use to keep track of where we are in each array
        left_copy_index = 0
        right_copy_index = 0
        sorted_index = left_index

        # Go through both copies until we run out of elements in one
        while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

            # Assess which array has the smaller value, store that value in the sorted array, then increment the counter and repeat
            if left_copy[left_copy_index] <= right_copy[right_copy_index]:
                array[sorted_index] = left_copy[left_copy_index]
                left_copy_index += 1
            else:
                array[sorted_index] = right_copy[right_copy_index]
                right_copy_index += 1

            # Iterate sorted array counter to store next element
            sorted_index += 1

        # Ran out of elements either in left_copy or right_copy, so go through the remaining elements and add them to sorted array
        while left_copy_index < len(left_copy):
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
            sorted_index += 1

        while right_copy_index < len(right_copy):
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
            sorted_index += 1
    
  
arr = [4,8,7,2,11,1,3]
merge = Solution() 
print ("Given array is: " + str(arr)) 
merge.merge_sort(arr,0,len(arr)-1) 
print ("Sorted array is: " + str(arr)) 

