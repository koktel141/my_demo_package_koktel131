import sys

print("New update (0.0.5) !")

def hello():
    if len(sys.argv) > 1:
        print(f"Hello {sys.argv[1]}!")
    else:
        print("Hello User!")
    
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

def days_to_nowruz():
    from datetime import date
    nowruz = date(2026, 3, 20) # تاریخ حدودی
    today = date.today()
    diff = nowruz - today
    print(f"Only {diff.days} days left until Nowruz!")
    
def menu():
    print("--- Welcome to My Package ---")
    print("1. Say Hello")
    print("2. Days to Nowruz")
    print("3. Add Numbers")
    
    choice = input("What do you want to do? (1/2/3): ")
    
    if choice == "1":
        hello()
    elif choice == "2":
        days_to_nowruz()
    elif choice == "3":
        pass