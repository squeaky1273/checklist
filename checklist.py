print("Hello World")
#my_fun_function('Hello World')


# Create
#checklist = list()
#checklist.append('Blue')
#print(checklist)
#checklist.append('Orange')
#print(checklist

# Read
#checklist[0]
#return checklist[0]

# Update
#checklist[1] = 'Cats'
#print(checklist)

# Destroy
#checklist = ['Blue', 'Cats']
#print(checklist)




# Create our checklist
checklist = []

# Define Functions
def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[int(index)] = str(item)

def destroy(index):
    checklist.pop(int(index))

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1
def mark_completed(index):
    item = checklist[index]

    if item[0] != "*":
        checklist[index] - "*" + checklist[index]
        return ("Completed")

def select(function_code):
    if function_code == "A":
        input_item = user_input("Input item: ")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?: ")
        destroy(item_index)

    elif function_code == "P":
        list_all_items()

    elif function_code == "C":
        item_index = user_input("Index number?: ")
        mark_completed(item_index)


    elif function_code == "Q":
        return False

    else:
        print("Unknown Options")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    checklist.append('purple socks')
    print(checklist)
    checklist.append('red cloak')
    print(checklist)
    checklist.append('green shoes')
    print(checklist)
    checklist.append('yellow shirt')
    print(checklist)
    checklist.append('pink pants')
    print(checklist)

    print(read(0))
    print(read(1))
    print(read(2))
    print(read(3))
    print(read(4))

    update(4, 'pink pants')

    destroy(1)

    print(read(0))

    #list_all_items()
    #select("C")
    #list_all_items()
    #select("R")
    #list_all_items()
    #select("P")
    #elect_all_code()

    user_value = user_input("Please Enter a value: ")
    print(user_value)
test()
running = True
while running:
    selection = user_input("Press A to add to list, R to remove from list, P to display list, C to mark as complete, and Q to quit: ")
    running = select(selection)
