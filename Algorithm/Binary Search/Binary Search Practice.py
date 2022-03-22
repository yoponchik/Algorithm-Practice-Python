#1:  State the problem clearly. Identify the inputs and the outputs
#Given a rotated list that was previously sorted, we need to find the MINIMUM number of times it was rotated
# The input would be an array of numbers e.g. num: [7,9,3,5,6]
#Output would be the number of times the sorted list was rotated e.g. 2


#2: Create the function
""" class BinarySearchPractice:
    def countRotations(nums):
        pass  """


#3. Make different cases
test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

nums0 = test0['input']['nums']
output0 = test0['output']

""" result0 = BinarySearchPractice.count_rotations(nums0)
print(result0, result0 == output0)    #should be None False, because right now we only did pass, and 3 != null
 """
#4: Create Test Case Checker
""" class BinarySearchPractice:
    def checkResult(tests):
        testNumber = 1
        for test in tests:
            input = tests['input']['nums']
            output = tests['output']
            print("Test", testNumber)
            if(output == BinarySearchPractice.countRotations(input)):
                print("PASS")
            else: 
                print("FAIL")
            testNumber += 1


    def countRotations(nums):
        pass 
    

BinarySearchPractice.checkResult(test) #should say FAIL """

#5 Add more test cases
tests = []
#initial case
tests.append(test0)
#list of size 8 rotated 5 times
tests.append({'input': {'nums': [4,5,6,7,8,1,2,3]}, 'output': 5})
#list not rotated
tests.append({'input': {'nums': [1,2,3,4,5]}, 'output': 0})
#list rotated once
tests.append({'input': {'nums': [7,3,5]}, 'output': 1})
#list that was rotated n-1 times, where n is size of the list
tests.append({'input': {'nums': [2,3,4,5,1]}, 'output': 4})
#list that was rotated n times, where n is size of the list
tests.append({'input': {'nums': [3,5,7,8,9,10]}, 'output': 0})
#empty list
tests.append({'input': {'nums': []}, 'output': 0})
#list containing just one element 
tests.append({'input': {'nums': [1]}, 'output': 0})

""" 
BinarySearchPractice.checkResult(test0, nums0)  #should say FAIL """


#6 Apply Brute Force Algorithm
#pattern: Since it was previously a SORTED array, rotating the array makes it so that the number
#of the index of the smallest number gives the number of times the array was rotated

""" class BinarySearchPractice:
    def countRotations(nums):
        position = 0                       #Initial position

        while position < len(nums):              #When should the loop be terminated
            #Check if the number at the current position is smaller than its predecessor
            if position > 0 and nums[position] < nums[position - 1]:             #if we are at position greater than 0 AND #number in current position is smaller than the one before it                                                                            
                return position                  #position gives the number of rotations
            
            position += 1          #add 1 to position             # FYI: if nums[0] then skips to position = 1
        return 0                    #what if no positions passed the check
            
    def checkResult(tests):

        testNumber = 0

        for test in tests:
            input = test['input']['nums']
            output = test['output']
    
            print("Test", testNumber)
            if(output == BinarySearchPractice.countRotations(input)):
                print("PASS")
            else: 
                print("FAIL")
            
            testNumber += 1

BinarySearchPractice.checkResult(tests) """


#7 Optimize Code
class BinarySearchPractice:
    def countRotations(nums):
        head = 0                                    #assign a variable for the head of the array
        tail = len(nums) - 1                        #assign a variable for the tail of the array

        while head < tail:                              #when should the loop be terminated?
            mid = (head + tail) //2                     # we use // to make it into integer
            midNumber = nums[mid]

            #if the mid has the answer
            if(mid > 0 and midNumber == min(nums)):                       #we don't do mid > head, because head can be updated
                return mid
            #if the answer is in the left half; mid < tail
            elif(mid < tail):       
                tail = mid - 1                        #we don't need to return hi or lo, because
            #if the answer is in the right half; mid > tail
            else:                       
                head = mid + 1
        return 0                    #what if no positions passed the check
            
    def checkResult(tests):

        testNumber = 0
        for test in tests:
            input = test['input']['nums']
            output = test['output']
            print("\nTest", testNumber)
            if(output == BinarySearchPractice.countRotations(input)):
                print("PASS")
            else: 
                print("FAIL")
            testNumber += 1

BinarySearchPractice.checkResult(tests)