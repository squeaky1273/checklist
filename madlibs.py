def create():
    inputs = ['interjection', 'name', 'place', 'verb', 'noun', 'adjective', 'color']

    interjection = input("Enter an interjection (expressive word): ")
    name = input("Enter your name: ")
    place = input("Enter a place: ")
    veb = input("Enter a verb ending in -ing")
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    color = input("Enter a color: ")
create()
def read():
    print(inputs(0) + "! My name is " + inputs(1) + ". I have a weird story to tell you. ")
    print("I was on my way to the " + inputs(2) + ".")
    print("While " + inputs(3) + ", I saw a truck. ")
    print("The truck that I saw was so peculiar because it reminded me of a " + inputs(4) + ".")
    print("The wheels were " + inputs(5) + " and the whole thing was the color, " + inputs(6) + ".")
read()
