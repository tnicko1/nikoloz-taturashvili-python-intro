input_string = input("Enter a string: ")

characters = []

for character in input_string:
    characters.append(character)

character_count = {}

for character in characters:
    if character in character_count:
        character_count[character] += 1
    else:
        character_count[character] = 1

for key, value in character_count.items():
    print(f"{key} - {value}")