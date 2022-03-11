#Binary Search
#https://jovian.ai/aakashns/python-binary-search
#https://www.youtube.com/watch?v=Jh4t9o2y_pw


#Regular Search
#Step 1-1: Create a function, with the input and the outputs in mind
""" class Search:
    def LocateCard(cards, query):
        pass """


#Step 1-2: Write out the test cases, to test if the inputs and the outputs will coincide
""" #test case
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

print(Search.LocateCard(cards, query) == output)  """

#dictionary test case                                           //can use dictionary to make it easier to test
test = {
        'input': {
            'cards': [0,1,3,4,5,7,9],
            'query': 7
        }, 
        'output': 5
    }

""" #does the output of the binary search  using the two keys equal to the expected output
print(Search.LocateCard(test['input']['cards'], test['input']['query']) == test['output']) 
print(Search.LocateCard(**test['input']) == test['output']) """                 



#Step 1-3: Think of all the Edge Cases
""" tests = []
#initial test case
tests.append(test)
#query in the middle case
tests.append({"input": { "cards": [13, 11, 12, 10, 5], "query": 12}, 'output': 2})
#query in the first element case
tests.append({"input": { "cards": [4, 2, 1, -1, 0], "query": 4}, 'output': 0})
#query in the last element case
tests.append({"input": { "cards": [3, -1, -9], "query": -9}, 'output': 2})
#only one element
tests.append({"input": { "cards": [6], "query": 6}, 'output': 0})
#repeated number in the cards
tests.append({"input": { "cards": [4, 5, 5, 5, 0], "query": 5}, 'output': 1})
#no query in cards
tests.append({"input": { "cards": [4, 1, 2, 3, 4], "query": 5}, 'output': -1})
#empty cards
tests.append({"input": { "cards": [], "query": 5}, 'output': -1})
#print(tests) """


#Step 1-4: Brute Force
""" class Search:
    # there are two inputs: the array of cards, and the query-> number you want
    def LocateCard(cards, query):
        #create POSITION == 0
        position = 0
        
        #Set up a loop
        while True:
            #Check if the element at the current position matches the query
            if(cards[position] == query):
                return position
            #Increment the position
            position +=1
            #Check if twe reached the end of the array
            if(position == len(cards)):               #this works because the array is # of elements, but the indices == (elements - 1)
                #Number not found
                return -1

    def TestFunction(tests):
        number = 0
        for test in tests:
            number += 1
            print("Test Number ", number)
            if(test['output'] == Search.LocateCard(**test['input'])):
                print("PASS")
            else:
                print("FAIL")
 """

#Step 1-5-1: Test with the first test case
""" result = Search.LocateCard(**test['input']) """

#Step 1-5-2: Test with all cases
""" Search.TestFunction(tests) """

#Step 1-6: Log Everything
""" class BinarySearch:
    def LocateCard(cards, query):
        position = 0

        #Log all the inputs 
        print('cards:', cards)
        print('query:', query)
        
        while True:
            if(cards[position] == query):
                return position
            position +=1
            if(position == len(cards)):               
                return -1

    def TestFunction(tests):
        number = 0
        for test in tests:
            number += 1
            print("Test Number ", number)
            if(test['output'] == Search.LocateCard(**test['input'])):
                print("PASS")
                print("----------------")

            else:
                print("FAIL")
                print("----------------")


Search.TestFunction(tests)                        #You can see that the Test Number 8 has an empty array
 """



#Step 1-7: Debug
""" class Search:
    def LocateCard(cards, query):
        position = 0

        #Log all the inputs 
        print('cards:', cards)
        print('query:', query)
        
        while (position < len(cards)):                          #prevent position from leaving end of the index
            if(cards[position] == query):
                return position
            position +=1          
        return -1

    def TestFunction(tests):
        number = 0
        for test in tests:
            number += 1
            print("Test Number ", number)
            if(test['output'] == Search.LocateCard(**test['input'])):
                print("PASS")
                print("----------------")

            else:
                print("FAIL")
                print("----------------")


Search.TestFunction(tests)  
 """


#Binary Search  - Assuming we have a SORTED LIST
#Step 2-1: List Cases
tests = []
#initial test case
tests.append(test)
#query in the middle case
tests.append({"input": { "cards": [2,3,6,7,8,10,11], "query": 7}, 'output': 3})
#query in the first element case
tests.append({"input": { "cards": [2,3,6,7,8], "query": 2}, 'output': 0})
#query in the last element case
tests.append({"input": { "cards": [0,5,8,9,10,16], "query": 16}, 'output': 5})
#only one element
tests.append({"input": { "cards": [6], "query": 6}, 'output': 0})
#repeated number in the cards
tests.append({"input": { "cards": [4, 5, 5, 5, 6, 6, 12], "query": 5}, 'output': 1})
#no query in cards
tests.append({"input": { "cards": [1,2,3,4,5,6,7,8], "query": 9}, 'output': -1})
#empty cards
tests.append({"input": { "cards": [], "query": 5}, 'output': -1})
#print(tests)


#Step 2-2: Implement Algorithm

""" class BinarySearch:
    def LocateCard(cards, query):
        head = 0                    #at the first index
        end = (len(cards) - 1)      #at the last index

        print("Cards: ", cards, "Query: ", query)

        while(head <= end):         #if the head is greater than the end, then that means we searched through the whole array; they passed each other
            midIndex = (head + end) // 2     #floor division: rounds result to nearest integer; because we int for array elements
            midNumber = cards[midIndex]
            print("head: ", cards[head], " end: ", cards[end], " mid_number: ", midNumber)

            if(query == midNumber):
                return midIndex                  #printing the mid, not the element in the index
            elif(query < midNumber):        #If number on the right side: move the end to right before the mid
                end = midIndex - 1
            elif(query > midNumber):
                head = midIndex + 1
        return -1

    def TestFunction(tests):
        number = 0
        for test in tests:
            number += 1
            print("Test Number ", number)
            print("Function Output", BinarySearch.LocateCard(**test['input']))
            print("Correct Output", test['output'])
            if(test['output'] == BinarySearch.LocateCard(**test['input'])):
                print("PASS")
                print("----------------")

            else:
                print("FAIL")
                print("----------------")


BinarySearch.TestFunction(tests)                                        #test #6 will probably fail, because there are multiple numbers that match the query
 """

#Step2-3: Debug - Because we have a SORTED list, we just have to check the adjacent indices to decide whether to go down or up
class BinarySearch:
    def LocateCard(cards, query):
        head = 0                    
        end = (len(cards) - 1)      

        while(head <= end):         
            midIndex = (head + end) // 2     
            result = BinarySearch.TestLocation(cards, query, midIndex)

            if(result == 'found'):
                return midIndex                 
            elif(result == 'left'):        
                end = midIndex - 1
            elif(result == 'right'):
                head = midIndex + 1

        return -1

    def TestLocation(cards, query, midIndex):
        midNumber = cards[midIndex]
        print('mid: ', midIndex, 'midNumber', midNumber)
        if(query == midNumber):     #2 conditions to check if they are equal: Are there multiple numbers equal to the query? If yet, go left to get the first one. If not, we found it
            if((cards[midIndex - 1] == query) and ((midIndex - 1) >= 0)):              #if the INDEX left of the mid has an element equal to query and it is greater or equal to 0 (to prevent from going out of INDEX)
                return 'left'
            else: 
                return 'found'
        elif(query < midNumber): #if the query is less than the midNumber, go left
            return 'left'
        else:                       #if the query is greater than the midNumber, go right
            return 'right'
        



    def TestFunction(tests):
        number = 0
        for test in tests:
            number += 1
            print("Test Number ", number)
            print("Function Output", BinarySearch.LocateCard(**test['input']))
            print("Correct Output", test['output'])
            if(test['output'] == BinarySearch.LocateCard(**test['input'])):
                print("PASS")
                print("----------------")

            else:
                print("FAIL")
                print("----------------")


BinarySearch.TestFunction(tests)
