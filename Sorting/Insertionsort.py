class Solution:
    def Insertionsort(self, array):
        
        # Start at 1 since first element is algorithm initializer  
        for index in range (1,len(array)):
            currentValue = array[index] # Temporarily store current value 
            currentPosition = index

            """
            While the preceeding array value is greater than current value, copy preceeding value to current value, iterate backward and assess again.
            Continue this process until iterator reaches beginning of list, or prior element is < current 
            """
            while currentPosition > 0 and array[currentPosition - 1] > currentValue:
                array[currentPosition] = array[currentPosition - 1]
                currentPosition = currentPosition - 1

            # Once optimal position is found, replace that element with the current value
            array[currentPosition] = currentValue

array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
sort = Solution()
sort.Insertionsort(array)
print(array)