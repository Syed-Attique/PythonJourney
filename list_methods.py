def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            # .pop() removes and returns the last item from the list
            undone = history.pop()
            print(f"Undone: '{undone}'")
        elif action == "Restart":
            # .clear() removes all items from the list, making it empty
            history.clear()
        else:
            # .append(item) adds a single item to the end of the list
            history.append(action)

        print(history)


main()