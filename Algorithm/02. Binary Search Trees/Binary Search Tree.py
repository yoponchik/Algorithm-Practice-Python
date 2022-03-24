#01. Create an empty program

""" class BinarySearchTree:
    class User:
        pass
 """

#This is called an Instantiation. We are instantiating an object of the class by calling it like a function.
""" user1 = BinarySearchTree.User()  """         

""" print(type(user1))   """   #should say class '__main__.BinarySearchTree.User     

#At the moment, the user1 object has no useful information. So, we use a constructor to construct an object

#O2. Constructors

""" class BinarySearchTree:
    class User:
        def __init__(self, username, name, email):
            self.username = username
            self.name = name
            self.email = email
            print("User Created!")


user1 = BinarySearchTree.User('yoponchik', 'Yo Ponchik', 'yoponchik@yoponchik.yoponchik')
    #a. An empty object of type User is created and stored in variable user1
    #b. init method called
    #c. The method passes user1 object as self, and passes the rest of the arguments as part of the self

 """

 #03. Adding more methods
""" class BinarySearchTree:
    class User:
        def __init__(self, username, name, email):   #Constructor
            self.username = username
            self.name = name
            self.email = email
            print("User Created!")
        def IntroduceYourselfTo(self, guestName):     #Method
            print("Hi {}, I'm {}! Contact me at {}.".format(guestName, self.name, self.email))

user2 = BinarySearchTree.User("John", 'John Doe', "john@doe.com")       #Object Instantiated
user2.IntroduceYourselfTo("Jane") """


#04. Str and Rpr Method
""" class BinarySearchTree:
    class User:
        def __init__(self, username, name, email):   #Constructor
            self.username = username
            self.name = name
            self.email = email
            print("User Created!")

        def __repr__(self):
            return "User(username = '{}', name = '{}', email = '{}')".format(self.username, self.name, self.email)
        
        def __str__(self):
            return self.__repr__()


user3 = BinarySearchTree.User("Jane", 'Jane Doe', 'jane@doe.com')
print(user3) """


#05 Output Methods + Create Sample Users
""" class BinarySearchTree:
    class User:
        def __init__(self, username, name, email):   #Constructor
            self.username = username
            self.name = name
            self.email = email
            print("User Created!")

        def __repr__(self):
            return "User(username = '{}', name = '{}', email = '{}')".format(self.username, self.name, self.email)
        
        def __str__(self):
            return self.__repr__()

    class UserDatabase:
        def Insert(self, user):
            pass
        def Find(self, username):
            pass
        def Update(self, user):
            pass
        def ListAll(self):
            pass """


#Instantiate Sample Users
josh = BinarySearchTree.User("josh", "Josh Bartkoske", "josh@bartkoske.com")
jake = BinarySearchTree.User("jake", "Jake Dibble", "jake@dibble.com")
joe = BinarySearchTree.User("joe", "Joe White", "joe@white.com")
james = BinarySearchTree.User("james", "James Gilbert", "james@gilbert.com")
daniely = BinarySearchTree.User("daniey", "Daniel Yilmaz", "daniel@yilmaz.com")
paul = BinarySearchTree.User("paul", "Paul Oh", "paul@oh.com")
danielk = BinarySearchTree.User("danielk", "Daniel Kim", "daniel@kim.com")
alec = BinarySearchTree.User("alec", "Alec Savig", "alec@savig.com")
noah = BinarySearchTree.User("noah", "Noah Palm", "noah@palm.com")
jonny = BinarySearchTree.User("jonny", "Jonny Sieberhagen", "jonny@sieberhagen.com")
david = BinarySearchTree.User("david", "David Kim", "david@kim.com")
austin = BinarySearchTree.User("austin", "Austin Davis", "austin@davis.com")
simeon = BinarySearchTree.User("simeon", "Simeon Blanc", "simeon@blanc.com")

#store users in array
users = [josh, jake, joe, james, daniely, paul, danielk, alec, noah, jonny, david, austin, simeon]


#06. Algorithm
#Insert: Loop thru the list and add new user by sorting it
#Find: Loop thru the list and find the user object with the username matching the query
#Update: Loop thru list, find the user object matching the query and update the details
#List: Return the list of user objects

#Can use <, >, == operators for usernames

""" print("ab" < "ac") """  #should be true, because in alphabetical order, ab is "less"

class BinarySearchTree:
    class User:
        def __init__(self, username, name, email):   #Constructor
            self.username = username
            self.name = name
            self.email = email
            print("User Created!")

        def __repr__(self):
            return "User(username = '{}', name = '{}', email = '{}')".format(self.username, self.name, self.email)
        
        def __str__(self):
            return self.__repr__()

    class UserDatabase:
        def __init__(self):             #constructor: Doesn't take any additional arguments apart from self
            self.users = []             #set a property users to self; set to empty array
        
        def Insert(self, user):
            i = 0
            while i < len(self.users):
                #find the first username in ARRAY USERS greater than the new user's username
                if(self.users[i].username  > user.username):
                    break                   #if you do find it; break out of while loop and insert user at position
                i +=1                       #go to next index
            self.users.Insert(i, user)      #

        def Find(self, username):
            for user in self.users:
                if(user.username == username):
                    return user
       
        def Update(self, user):
            target = self.Find(user.username)
            target.name, target.email = user.name, user.email
       
        def ListAll(self):
            return self.users               #return the whole array