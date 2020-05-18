#Classic quicksort - chooses the first element in the array as the pivot point and sorts accordingly 
class Solution:
    def partition(self, array, start, end):
        # [start|low_ _ _ _ _ _high] --> Three pointers 
        pivot = array[start]
        low = start + 1
        high = end 

        while True:
            # Continue iterating high and low pointers toward each other until an unsorted value is found or if pointers cross each other
            while low <= high and array[low] <= pivot: 
                low = low + 1

            while low <= high and array[high] >= pivot:
                high = high - 1

            # If both pointers have unsorted values, swap them into correct position, else if they have crossed each other, break
            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break
        
        # Sort the pivot value into its respective place by switching with high/low pointer
        array[start], array[high] = array[high], array[start]

        return high # Note: values are swapped, but pointer locations are the same! Return the location of the now sorted pviot
    
    def quicksort(self,array,start,end): 
        if start >= end:
            return
        
        p = self.partition(array, start, end) #Retrieves the index of the pivot point after each sort
        self.quicksort(array, start, p-1) #Recursively sorts array on left side of the pivot
        self.quicksort(array, p+1, end) #Recursively sorts array on right side of the pivot



array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
quick = Solution()
quick.quicksort(array, 0, len(array)-1)
print(array)