words = ['interjection', 'name', 'location', 'verb', 'noun', 'adjective', 'color']
def create():
    words[0] = input("Enter an interjection: ")
    words[1] = input("Enter a name: ")
    words[2] = input("Enter a location: ")
    words[3] = input("Enter a verb ending in -ing: ")
    words[4] = input("Enter a noun: ")
    words[5] = input("Enter an adjective: ")
    words[6] = input("Enter a color: ")
create()

def read():
    print(words[0] + "! My name is " + words[1] + ". I have a weird story to tell you. ")
    print("Yesterday, I was on my way to (the) " + words[2] + " for fun.")
    print("While " + words[3] + ", I saw a truck. ")
    print("The truck that I saw was so peculiar because it reminded me of a(n) " + words[4] + ".")
    print("The wheels were " + words[5] + " and the entire thing was the color, " + words[6] + ".")
read()
