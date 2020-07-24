#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) runtime is O(n)
because if we assume that n = 4 
so the loop depends in the size of n linearly   
while a < 4*4*4:
    a = 0 + 4*4 
    print(a)
output:
16
32
48
64
this will run 4 times  linearly 


b) runtime is n log(n)
because the nested while loop inside the for loop will make it run by 
doubling the size of j that the nested loop depends on


c) ) runtime is O(n)
     because of the recursive function that technically relies of the input size
     of bunnies(n size)

## Exercise II
#plenty of eggs 
#building with number of floors 
<!-- USING BINARY SEARCH ; DO IT AGAIN -->
since, floors start for floor 1 up to N number of floors 
to maximize the number of the broken eggs and find the floor that eggs stated 
getting broken at w need to start form the them middle 
def binary_search(arr, target, start, end):


middleFloor = (first_floor + last_floor) // 2
check if the floor is in the middle
while eggs dont get broke:
     if floors[middleFloor] == f:
        <!-- then we are on the right spot 
         which is the middle floor -->
        return middleFloor
    if floors[middleFloor] < f:
     <!-- start for form the middle  -->
     first_floor = middleFloor + 1
    
    else:
     last_floor = middleFloor - 1

in this case we are minimize our searching and find the right spot quickly 
and also this helps to minimize the number of eggs that get broken 

since the eggs depends on number of floors
then our search is also depends linearly on it as well
so the runtime complexity is O(n)
