#Andrey Ilkiv Assignment 6 Problem 2 Section 01

print("Part A ---------------------------------------")
mylist = [10, 20, 30] #my list
def listlen(mylist):    #function for getting length of list
    count = 0             #count set to 0 by default
    for i in mylist :      # for every index in my list add 1
        count += 1
    print(count)        # print total after going through the list
listlen(mylist)         # uses the function in maid method

print("Part B ---------------------------------------")
mylist2 = [10, 20, 30, 5, 3]    #mylist
def listmax(mylist2):               #function for finding max in list
    largest = 0                         # largest set to 0 by default
    for j in mylist2:                   # sets the largest known index until a bigger one is found start s at 0
        if j > largest:
            largest = j
    print(largest)                      #prints largest list item
    print(mylist2)                      #prints original list
listmax(mylist2)                    #uses function in main

print("Part C ---------------------------------------")
mylist3 = [10, 20, 30]          #my list
def listcopy(mylist3):          #function for copying a list
    copyoflist = [] + mylist3   #newlist = to empty list + original list = copied list
    print(copyoflist)               # prints copy of the original list
listcopy(mylist3)                   #uses function in main

print("Part D ---------------------------------------")
mylist4 = [10, 20, 30]          #my list
def listappend(mylist4, inp):   #function for listappend
    answer = inp                    # takes value input and sets it to a variable
    y = mylist4 + [answer]      # adds new variable to the end of original list
    print(("[{0}]".format(', '.join(map(str, y)))))     #formats the list to remove anything besides [ , ] used for removing single qoutes and prints final product
listappend(mylist4, 999)                                    # uses function in main, takes in list and value

print("Part E ---------------------------------------")
mylist5 = [10, 20, 30]      #my list
def listinsert(mylist5, index, value):  #function for inserting into a list at given index
    newlist = mylist[:index] + [str(value)] + mylist[index:]    #breaks list in half at the chosen value and adds list string object then adds the rest of the original list
    print(("[{0}]".format(', '.join(map(str, newlist)))))           #formats list to show properly and prints
    print(mylist5)                                                                  # prints original list
listinsert(mylist5, 1, 999)                 # uses function in main with list, index value, and value

print("Part F ---------------------------------------")
mylist6 = [10, 20, 30]      #mylist
def listremove(mylist6, char):      #function for removing specific item from entire list
    newlist2 = [s for s in mylist6 if s != char]    #creates new list that does not include the character entered
    print(newlist2)                                             #prints new list without value chosen
    print(mylist6)                          #prints original list
listremove(mylist6, 20)                 #uses function in main

print("Part G ---------------------------------------")
mylist7 = [10, 20, 30]              #my list
def listreverse(mylist7):           #function for reversing the list
    newlist3 = mylist7[::-1]        # creates new list and splits its twice then moves it to the left once to flip 10 and 30
    print(newlist3)         #prints new list in reverse
    print(mylist7)          #prints original list
listreverse(mylist7)    # uses function in main
