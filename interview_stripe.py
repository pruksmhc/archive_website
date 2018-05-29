
 # [ 2 3 8 11 ]  - sort these
 # fill up from smallest to largest. 
 #  smallest_min
 # min = 1
 # return 1 - find_min(curr_min)
# [1 7 ]
# hashing  


# here, find the next minimum. 
# find the next allocated thing to find. 
# and then insert this in. 

"""
 Write a function which, given the list of currently allocated server numbers, 
 returns the number of the next server to allocate. In addition, you should demonstrate your approach to testing that 
 your function is correct. You may choose to use an existing testing library for your language if you choose, or you 
 may write your own process if you prefer.  
"""

# Heap method = O(logn(n)) 
# Keeping track of a pointer - O(1) for everything. O(log(n)) for inserting 
# O(lo(n) for finding it and then O(n) for shifting. )
# Also for a heap, for pYthon's heapq, it doens't support searching or deleting, so you just 
# have to dletee using the normal list methods of remove() 
# In python, the class Queueu is. put and get, not enqueue and dequeue. 


import unittest 

def find_next_min(servers):
   if (servers is None):
      raise TypeError("Please put in a valid server")
   for i in range(1, len(servers)):
     if ((servers[i] - servers[i-1]) > 1):
       return  servers[i-1] + 1
   return -1

class TestServerAllocations(unittest.TestCase):
   def test_allocation(self):
      self.assertEqual(find_next_min([1,2,5,7]), 3)
      with self.assertRaises(TypeError) as cm:
         find_next_min(None)
      self.assertIn(3, [find_next_min([1,2,5,7])]) 

      self.assertEqual(find_next_min[1,2,3,4], 3)
      
# assertEquals, assertRaises -TypeErorr  assertTrue
# assertNotEqual assertIn, assertNotIn 

if __name__ == '__main__':
    unittest.main()
