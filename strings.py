# 1. Write a Python program to find the median of two sorted arrays.

def sorted_arrays(nums1, nums2):          #take the array the is already sorted    
    nums = sorted(nums1 + nums2)
    n = len(nums)                   #find it's len is even
    
    if n % 2 == 0:                                    #check if the array is divisible by two
        return (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        return nums[n//2]
    
nums1 = [3, 5]
nums2 = [6, 8]
print(sorted_arrays(nums1, nums2))


# 2. Write a Python program to find the largest element in an unsorted array.

def element(arrys):
    largest = arry[0]                       #check if the largest array id equal to element zero   
    for i in range(1, len(arry)):          #loop through the array to check its len
        if arry[i] > largest:              #if the array is greater than the largest you return the largest
            largest = arry[i]
    return largest
arry = [23, 56, 34, 12]
print(element(arry))


# # 3. Write a Python program to find the first missing positive integer in an unsorted array.

def positive(arry):
    arry = list(set(arry))                #use set to remove duplicates since set doesn't support duplicates
    arry.sort()                          #sort the arrays in ascending order
    smallest = 1
    for i in arry:                       #loop though the array to find yhe smallest value
        if i == smallest:
            smallest += 1
    return smallest                      #return the array and then print it out         
arry = [56, 67, 34, 23, 89, 12, 31]
print(positive(arry))



# 4. Write a Python program to reverse an array of integers.
#(using string slicing)

lst = [10, 31, 22, 53, 14, 5]
lst.reverse()                          #use .reverse inbuilt function to print the letters from the end
print(lst)



#                     SOME OF THE TAKE AWAYKEYS I GAINED INCLUDE
# 1. Arrays in Kotlin are represented by the Array class, which is generic over the type of the array elements.

# 2. Kotlin supports string templates, which allow you to embed expressions in a string. To use a string template, enclose the expression in ${}.

# 3. You can create an array using the arrayOf() function or the Array() constructor.








