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
checklist = list()

# Define Functions
def create(item):
    create("purple socks")
    create("red cloak")

def read(item):
    print(read(0))
    print(read(1))

def update(index, item):
    update(0, "purple socks")

def destroy(index):
    destroy(1)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(index + list_item)
        index += 1
#def mark_completed(index):


#def select(function_code):

#def user_input(prompt):

def test():
    create("purple socks")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()
    print("{} {}".format(index, list_item))
