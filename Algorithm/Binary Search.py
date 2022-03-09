#Binary Search
#https://jovian.ai/aakashns/python-binary-search
#https://www.youtube.com/watch?v=Jh4t9o2y_pw

class BinarySearch:
    def locate_card(cards, query):
        pass


#test case

#cards = [13, 11, 10, 7, 4, 3, 1, 0]
#query = 7
#output = 3

#result = BinarySearch.locate_card(cards, query)
#print(result)
#result == output

#dictionary test case
test = {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
        }, 
        'output': 3
    }

print(BinarySearch.locate_card(**test['input']) == test['output'])
#BinarySearch.locate_card(test['input']['cards'], test['input']['query']) == test['output']

