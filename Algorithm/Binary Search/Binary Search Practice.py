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
    def checkResult(tests, nums):
        output = tests['output']
        if(output == BinarySearchPractice.countRotations(nums)):
            print("PASS")
        else: 
            print("FAIL")


    def countRotations(nums):
        pass 
    

BinarySearchPractice.checkResult(test0, nums0) #should say FAIL """

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