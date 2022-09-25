#print("Hello from inside a file!")

def hello():
    print('Nothing!')
hello()

def pack(breakfast, lunch, dinner):
    return[breakfast, lunch, dinner]
print('breakfast, lunch, dinner')
    
food = [ 'apple', 'banana', 'cherry']

def eat_lunch(food):
    if len(food) == 0: #len(returns the # of characters in a string)
        print('My Lunchbox is empty')
    else: 
        for x in range(len(food)):
            if x == 0:
                print("First I eat", food[0] )
            else:
                print("Next I eat", food[x])
    
eat_lunch([])
eat_lunch(['beans'])
eat_lunch(["beans","rice", "chicken", "the tortillas"])







    