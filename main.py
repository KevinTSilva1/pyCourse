def nameCalculator(name):
    return len(name)

user_name = input("Please tell me your name : ")
print("Your name contains " + str(nameCalculator(user_name)) + " letters.")