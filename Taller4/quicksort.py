def quicksort(arr_in):
   # SImple routine for a quicksort
   # input: arr_in - array with numbers, unsorted
   #
   # output: arr - same array, but sorted
   #

   import numpy as np

   if (arr_in.ndim>1):
      print("Array is wrong dimensions")
      return None

   # Make a copy of the array
   arr = np.copy(arr_in)
   n   = arr.size

   for j in range(2,n+1):
      ibreak = 0
      A = arr[j-1]
      for i in range(j-1,0,-1):
         if (arr[i-1] <= A):
            arr[i] = A
            ibreak = 1
            break
         arr[i]=arr[i-1]
      if (ibreak==0):
         arr[0] = A
   return arr


