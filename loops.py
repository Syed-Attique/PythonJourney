def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver},
    
       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """


def while_loop_examples():
    print("\n--- While Loop Examples ---")

    # Example 1: Basic counter. Loops a specific number of times.
    print("1. Basic Counter:")
    count = 1
    while count <= 3:
        print(f"Count is {count}")
        count += 1
    
    # Example 2: Using 'break' to exit early. Great for searching or stopping early.
    print("\n2. Using 'break':")
    number = 0
    while True: # Infinite loop pattern
        if number == 2:
            print("Breaking the loop at 2!")
            break
        print(f"Number is {number}")
        number += 1

    # Example 3: Using 'continue' to skip an iteration and go to the next one.
    print("\n3. Using 'continue':")
    skip_count = 0
    while skip_count < 4:
        skip_count += 1
        if skip_count == 2:
            print("Skipping 2!")
            continue # Skips the print statement below and goes back to the condition
        print(f"Current count is {skip_count}")

    # Example 4: Processing items in a list until it is empty.
    print("\n4. Processing a list until empty:")
    tasks = ["Wash dishes", "Sweep floor", "Fold laundry"]
    while tasks: # Evaluates to True as long as the list is not empty
        current_task = tasks.pop(0)
        print(f"Completing task: {current_task}")


main()
while_loop_examples()