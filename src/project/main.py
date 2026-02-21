import sys

print("New update!")

def hello():
    if len(sys.argv) > 1:
        print(f"Hello {sys.argv[1]}!")
    else:
        print("Hello User!")
    
    # Start the main loop
    main_loop()

def main_loop():
    while True:
        choice = input("\nDo you want to add numbers? (yes/no): ").lower()
        
        if choice == "yes":
            calculate()
        elif choice == "no":
            print("Goodbye!")
            break  # This stops the loop and exits the program
        else:
            print("Please type 'yes' or 'no'.")

def calculate():
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(f"Result: {x} + {y} = {x + y}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")