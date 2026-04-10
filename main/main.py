# 1-m
nums = [5, 2, 9, 1, 7]

result = sorted(nums)
print(result)

# 2-m
nums = [5, 2, 9, 1, 7]

result = sorted(nums, reverse=True)
print(result)

# 3-m
words = ["banana", "apple", "cherry"]

print(sorted(words))

# 4-m
text = "python"

print(sorted(text))

# 5-m
words = ["apple", "kiwi", "banana"]

result = sorted(words, key=len)
print(result)

# 6-m

words = ["apple", "banana", "kiwi"]

result = sorted(words, key=lambda x: x[-1])
print(result)

# 7-m
nums = [-10, 5, -3, 2]

result = sorted(nums, key=abs)
print(result)

# 8-m
students = [("Ali", 85), ("Vali", 90), ("Sami", 80)]

# Ball bo‘yicha sort
result = sorted(students, key=lambda x: x[1])
print(result)

# 9-m
students = [("Ali", 85), ("Vali", 90), ("Sami", 80)]

# Ball bo‘yicha sort
result = sorted(students, key=lambda x: x[1])
print(result)

# 10-m
words = ["apple", "Banana", "cherry"]

result = sorted(words, key=str.lower)
print(result)

# 11-m
nums = [3, 1, 2]

# sorted
new_nums = sorted(nums)
print(nums)
print(new_nums)

# sort
nums.sort()
print(nums)

# 12-m
students = [
    {"name": "Ali", "age": 25},
    {"name": "Ali", "age": 20},
    {"name": "Vali", "age": 22}
]

# avval name, keyin age
result = sorted(students, key=lambda x: (x["name"], x["age"]))
print(result)

# 1-m
nums = [4, 1, 7, 3, 2]
result = sorted(nums)
print(result)
