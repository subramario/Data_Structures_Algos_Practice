#Classic quicksort - chooses the first element in the array as the pivot point and sorts accordingly 
class Solution:
    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end 

        while True:
            while low <= high and array[low] <= pivot:
                low = low + 1

            while low <= high and array[high] >= pivot:
                high = high - 1

            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break

        array[start], array[high] = array[high], array[start]

        return high
    
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