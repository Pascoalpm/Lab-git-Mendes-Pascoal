# Git Lab - Sample Program

def print_greeting():
name = input("What is your name?")
for i in range(3):
message = f"Hello, {name}! Greeting #{i+1}"
print(message)

print_greeting()