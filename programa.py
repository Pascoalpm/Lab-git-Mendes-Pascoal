# Git Lab - Sample Program

def print_greeting():
name = input("What is your name?")

if name == "":
print("Hello, Anonymous User!")
else:
for i in range(3):
message = f"Hello, {name}! Greeting #{i+1}"
print(message)

print("Program completed successfully!")

print_greeting()