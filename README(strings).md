# Python String Methods: A Quick Guide

Strings in Python are immutable sequences of characters. Python provides a rich set of built-in methods to manipulate and format strings.

Here are some of the most frequently used string methods with examples:

## 1. Changing Case

- **`.lower()`**: Converts all characters to lowercase.
- **`.upper()`**: Converts all characters to uppercase.
- **`.title()`**: Converts the first character of each word to uppercase (title case).
- **`.capitalize()`**: Converts only the very first character of the string to uppercase.

```python
text = "hello WORLD!"

print(text.lower())      # Output: hello world!
print(text.upper())      # Output: HELLO WORLD!
print(text.title())      # Output: Hello World!
print(text.capitalize()) # Output: Hello world!
```

## 2. Removing Whitespace

- **`.strip()`**: Removes leading and trailing whitespace (spaces, tabs, newlines).
- **`.lstrip()`**: Removes only leading whitespace (left side).
- **`.rstrip()`**: Removes only trailing whitespace (right side).

```python
dirty_string = "   Some text here   "

print(dirty_string.strip())  # Output: 'Some text here'
```

## 3. Splitting and Joining

- **`.split(separator)`**: Splits a string into a list of strings based on a separator (defaults to any whitespace).
- **`separator.join(iterable)`**: Joins an iterable (like a list) of strings into a single string, using the string it was called on as a separator.

```python
# Splitting
csv = "apple,banana,cherry"
fruits = csv.split(",")
print(fruits) # Output: ['apple', 'banana', 'cherry']

# Joining
words = ['Python', 'is', 'fun']
sentence = " ".join(words)
print(sentence) # Output: 'Python is fun'
```

## 4. Searching and Replacing

- **`.replace(old, new)`**: Replaces all occurrences of a substring with a new substring.
- **`.find(substring)`**: Returns the lowest index where the substring is found. Returns `-1` if not found.
- **`.startswith(prefix)`**: Returns `True` if the string starts with the given prefix.
- **`.endswith(suffix)`**: Returns `True` if the string ends with the given suffix.

```python
text = "I love apples"

print(text.replace("apples", "oranges")) # Output: 'I love oranges'
print(text.find("love"))                 # Output: 2
print(text.startswith("I"))              # Output: True
print(text.endswith("!"))                # Output: False
```

## 5. String Slicing

String slicing allows you to extract a portion of a string (a substring). The syntax is `string[start:stop:step]`.
- **`start`**: Index where the slice begins (inclusive). Defaults to `0`.
- **`stop`**: Index where the slice ends (exclusive). Defaults to the end of the string.
- **`step`**: Determines the increment between each index. Defaults to `1`.

```python
phone = "6174951000"

# Basic slicing: [start:stop]
print(phone[0:3])   # Output: '617' (Characters from index 0 up to, but not including, 3)
print(phone[6:10])  # Output: '1000' (Characters from index 6 up to 10)

# Omitting start or stop index
print(phone[:3])    # Output: '617' (Starts from the beginning to index 3)
print(phone[6:])    # Output: '1000' (Starts from index 6 to the end)
print(phone[:])     # Output: '6174951000' (Creates a full copy of the string)

# Negative indexing (counting from the end)
print(phone[-4:])   # Output: '1000' (Last 4 characters)
print(phone[:-4])   # Output: '617495' (Everything EXCEPT the last 4 characters)
print(phone[-7:-4]) # Output: '495' (From the 7th last to the 4th last)

# Using the step parameter: [start:stop:step]
print(phone[0:10:2]) # Output: '67910' (Every 2nd character)
print(phone[::2])    # Output: '67910' (Every 2nd character from the whole string)
print(phone[1::2])   # Output: '14500' (Every 2nd character starting from index 1)

# Reversing a string
print(phone[::-1])   # Output: '0001594716' (Reverses the entire string)
```

---

## Example from `string_methods.py`

In your `string_methods.py` file, we combine `.strip()`, `.title()`, and `', '.join()` to clean up a list of TV show names and print them out neatly.

### Code:
```python
SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family "
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        # .strip() removes the trailing space in "the Proud family "
        # .title() capitalizes the first letter of each word
        cleaned_shows.append(show.strip().title())
    
    # ', '.join() takes our list and turns it into a single string separated by commas
    print(', '.join(cleaned_shows))

main()
```

### Output:
```text
Avatar: The Last Airbender, Ben 10, Arthur, Spongebob Squarepants, Phineas And Ferb, Kim Possible, Jimmy Neutron, The Proud Family
```
