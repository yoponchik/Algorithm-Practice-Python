
#Queue = FIFO



class Queue:


    def Append():

        queue.append("a")
        queue.append("b")
        queue.append("c")

        print(queue)

        # ['a', 'b', 'c'] 


    #Removing elements from the queue = Dequeue
    def Dequeue():
        print(queue.pop(0))
        print(queue.pop(0))
        print(queue.pop(0))

        print(queue)

        #a
        #b
        #c
        #[]


#Stack = LIFO

class Stack:
    def Append():
        stack.append('a')
        stack.append('b')
        stack.append('c')

        print(stack)

        # ['a', 'b', 'c'] 

    def Pop():
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())
        
        print(stack)

        #c
        #b
        #a
        #[]



#Heap = Smallest Out

import heapq
class Heap:



    def Heapify():

        heapq.heapify(li)           #using heapify to convert list to heap
                                    #also orders them numerically

        print(list(li))

        #[2, 3, 9, 6, 5]

    def Push():
        heapq.heappush(li, 4)

        print(list(li))

        #[2, 3, 4, 6, 5, 9]

    def Pop():
        heapq.heappop(li)           #takes out the smallest number

        print(list(li))

        #[3, 5, 4, 6, 9]




queue = []
stack = []
li = [5,6,9,2,3]            #list

Queue.Append()
Queue.Dequeue()

Stack.Append()
Stack.Pop()

Heap.Heapify()
Heap.Push()
Heap.Pop()
