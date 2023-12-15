#This is stack function
def stack(myList, operation, new_element=None):
    if operation == 'add':
        if new_element == None:
            print("Error:Add a value")
        else:
            myList.insert(0,new_element)
            print("Adding new element to the stack")
            print(myList)

    elif operation == 'remove':
        myList.pop(0)
        print("Adding remove an element from stack")
        print(myList)

    else:
        print("Operation can be add and remove only")

#This is queue function
def queue(myList, operation, new_element=None):
    if operation == 'add':
        if new_element == None:
            print("Error:Add a value")
        else:
            myList.append(new_element)
            print("Adding new element to the queue")
            print(myList)
    elif operation == 'remove':
        myList.pop(0)
        print("Adding remove and element from queue")
        print(myList)




myList = [1,2,3,4]
stack(myList,'add',0)
stack(myList,'remove')
queue(myList,'add',5)
queue(myList,'remove')







