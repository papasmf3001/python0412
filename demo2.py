# List demo
fruits = ['apple', 'banana', 'orange', 'mango']

# Accessing elements
print(fruits[0]) # Output: apple
print(fruits[2]) # Output: orange

# Slicing
print(fruits[1:3]) # Output: ['banana', 'orange']

# Appending an element
fruits.append('grape')
print(fruits) # Output: ['apple', 'banana', 'orange', 'mango', 'grape']

# Removing an element
fruits.remove('banana')
print(fruits) # Output: ['apple', 'orange', 'mango', 'grape']


# Dict demo
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values
print(person['name']) # Output: John
print(person['age']) # Output: 30

# Adding a new key-value pair
person['occupation'] = 'Software Engineer'
print(person) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'Software Engineer'}

# Updating a value
person['age'] = 31
print(person) # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'occupation': 'Software Engineer'}

# Deleting a key-value pair
