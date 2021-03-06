class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #If n is an odd number, return n - 1 numbers and 0, where half are positve and the other half are the negative version of that number
        #If n is an even number, return n numbers, where half are positve and the other half are the negative version of that number

        
        return_list,counter = [],1

        while counter <= int(n/2) :
            return_list.insert(counter,counter)
            return_list.insert(counter+1,counter * -1)
            counter += 1
        
        if n % 2 != 0 :
            return_list.insert(n,0)
        
        return return_list
