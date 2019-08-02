# --- Define your functions below! ---
print(
'''
Hi I'm arshell the chatbot, how can I assit you today?
'''
)
# --- Put your main program below! ---
def main():
    yourname = input("Hi what's your name? ")
    says_hello(yourname)
    replies()
    joke()
def says_hello(name):
    print("hi " + name)
    your_day = input("tell me about yor day, how are you feeling? ")
    print("oh..")
def replies():
    preferences = input("cats or dogs?")
    if preferences == "dogs":
        print("omg same girl, they're so cute and fluffy")
    else:
        print("facinating.")
def joke():
    jk = input("i can tell you a joke")
    print("What is Harry Potter's favorite method of getting down a hill?")
    random = input("type here: ")
    print("Walking... jk, rolling.")
    jokes = input("hahaha that was funny right?")
    if "no" is jokes:
        print("uh that was rude")
    else:
        print("hahaha")

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
