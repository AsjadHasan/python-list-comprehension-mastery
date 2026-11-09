
"""
List Comprehension Mastery

Filter strings shorter than 4 characters
and convert the remaining strings to uppercase.
"""

words = ["apple", "bat", "cherry", "dog", "elderberry"]

# Filter and transform using list comprehension
result = [word.upper() for word in words if len(word) >= 4]

print("Original List:", words)
print("Filtered List:", result)
