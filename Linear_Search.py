import time

def linear_search(list1, item):
    
    for position in range(len(list1)):
        if alist[position] == item:
            print("Found what you are looking for.")
            time.sleep(2)
            print("You can find this at index:", position)
            return 1

if __name__ == "__main__":
    mylist = ['apple', 'banana', 'orange', 'grapes', 'guava']
    item = input("Enter the item: ")
    found = linear_search(mylist, item)
    if not found:
        print('Item is not in the list.')
