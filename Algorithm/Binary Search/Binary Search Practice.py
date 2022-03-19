#1:  State the problem clearly. Identify the inputs and the outputs
#Given a rotated list that was previously sorted, we need to find the number of times it was rotated
# The input would be an array of numbers e.g. num: [7,9,3,5,6]
#Output would be the number of times the sorted list was rotated e.g. 2


#2: Create the function
class BinarySearchPractice:
    def count_rotations(nums):
        pass 

#3. Make different cases
test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

nums0 = test['input']['nums']
output0 = test['output']

result0 = BinarySearchPractice.count_rotations(nums0)
print(result0, result0 == output0)    #should be None False, because right now we only did pass, and 3 != null
