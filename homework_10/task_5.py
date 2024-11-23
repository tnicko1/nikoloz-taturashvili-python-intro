"""
Write a function that takes a text and returns the text in reverse order.
Call the function several times with different arguments to demonstrate its operation.
"""

def inverted_text(text: str) -> str:
    return text[::-1]

# Test
print(inverted_text("hello"))  # Output: olleh
print(inverted_text("world"))  # Output: dlrow
print(inverted_text("Python"))  # Output: nohtyP
print(inverted_text("Programming"))  # Output: gnimmargorP
print(inverted_text("Language"))  # Output: egaugnaL