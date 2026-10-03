print("Program starting.")
print("String comparisons")
Word1=input("Insert first word: ")
Char=input("Insert a character: ")
if Char in Word1:
    print(f'Word "{Word1}"" contains character "{Char}"')
Word2=input("Insert second word: ")
if Char in Word2:
    print(f"Word '{Word2}' contains character '{Char}'")
if Word1<Word2:
    print(f'The first word "{Word1}" is before the second word "{Word2}" alphabetically.')
elif Word1>Word2:
    print(f'The second word "{Word2}" is before the first word "{Word1}" alphabetically.')
else:
    print(f'Both inserted words are the same alphabetically, "{Word1}"')
print("Program ending.")