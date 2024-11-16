words = ['Bakkers', 'Metacorp', 'Militech', 'Arasaka', 'Kendachi', 'KangTao', 'Kiroshi', 'Maelstrom', 'NetWatch', 'NUSA', 'Raven', 'SovOil', 'Trauma', 'Tyger Claws', 'Wraiths', 'Zetatech', 'Biotechnica']

filtered_words = [word.upper() for word in words if len(word) <= 3]

print("Original list of words:")
print(words)

print("\nFiltered list of words:")
if filtered_words:
    print(filtered_words)
else:
    print("No words found with 3 or fewer characters!")

print("\nSummary:")
print(f"Total words: {len(words)}")
print(f"Filtered words: {len(filtered_words)}")