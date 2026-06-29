# Python Dictionaries: A Complete Guide

A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key's value can be a number, a string, a list, or even another dictionary.

## 1. Creating a Dictionary

Dictionaries are wrapped in braces `{}`, with a series of key-value pairs inside.

```python
# Empty dictionary
my_dict = {}

# Dictionary with key-value pairs
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}
```

## 2. Accessing Values

To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets.

```python
print(person["first_name"])  # Output: John
```

Alternatively, use the `.get()` method, which returns `None` (or a default value) instead of an error if the key doesn't exist:

```python
print(person.get("age"))                 # Output: 30
print(person.get("country", "Unknown"))  # Output: Unknown
```

## 3. Adding or Modifying Values

You can add new key-value pairs or change existing ones by assigning a value to a key. 

> [!NOTE]
> You **cannot** use the `.append()` method on a dictionary. `.append()` is specifically for lists because lists just add a single item to the end of an ordered sequence. Dictionaries require both a **key** and a **value**, so you must use direct assignment (`person["job"] = "Developer"`) or the `.update()` method.

```python
# Modifying an existing value
person["age"] = 31

# Adding a new key-value pair using direct assignment
person["job"] = "Developer"

# Adding or updating multiple key-value pairs using .update()
person.update({"hobby": "Photography", "age": 32})

print(person)
# Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 32, 'city': 'New York', 'job': 'Developer', 'hobby': 'Photography'}
```

## 4. Removing Key-Value Pairs

There are several ways to remove items from a dictionary:

- **`del` statement**: Removes a specific key-value pair.
- **`.pop()` method**: Removes a specific key and returns its value.
- **`.clear()` method**: Empties the entire dictionary.

```python
# Using del
del person["city"]

# Using pop()
job = person.pop("job")
print(job) # Output: Developer

# Using clear()
person.clear()
print(person) # Output: {}
```

## 5. Looping Through a Dictionary

You can loop through a dictionary's keys, values, or both.

```python
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

# Looping through all key-value pairs using .items()
for word, points in WORDS.items():
    print(f"{word} is worth {points} points.")

# Looping through all keys using .keys() (or just iterating over the dictionary)
for word in WORDS.keys():
    print(word)

# Looping through all values using .values()
for points in WORDS.values():
    print(points)
```

## 6. Important Dictionary Methods

| Method | Description | Example |
| :--- | :--- | :--- |
| `.copy()` | Returns a copy of the dictionary | `new_dict = my_dict.copy()` |
| `.keys()` | Returns a view object containing the keys | `my_dict.keys()` |
| `.values()` | Returns a view object containing the values | `my_dict.values()` |
| `.items()` | Returns a view object containing a list of tuple pairs (key, value) | `my_dict.items()` |
| `.pop(key)` | Removes the element with the specified key | `my_dict.pop("name")` |
| `.update(dict)` | Updates the dictionary with the specified key-value pairs | `my_dict.update({"age": 25})` |
| `.clear()` | Removes all elements from the dictionary | `my_dict.clear()` |
