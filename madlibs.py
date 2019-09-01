words = ['interjection', 'name', 'place', 'verb', 'noun', 'adjective', 'color']
def test():
    words[0] = input("Enter an interjection: ")
    words[1] = input("Enter a name: ")
    words[2] = input("Enter a place: ")
    words[3] = input("Enter a verb ending in -ing: ")
    words[4] = input("Enter a noun: ")
    words[5] = input("Enter an adjective: ")
    words[6] = input("Enter a color: ")

    print(words[0] + "! My name is " + words[1] + ". I have a weird story to tell you. ")
    print("I was on my way to the " + words[2] + ".")
    print("While " + words[3] + ", I saw a truck. ")
    print("The truck that I saw was so peculiar because it reminded me of a " + words[4] + ".")
    print("The wheels were " + words[5] + " and the whole thing was the color, " + words[6] + ".")
test()
