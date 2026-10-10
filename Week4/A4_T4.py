print("Program starting.")
i=0
word_len = 0
while True:
    i+=1
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    word_len +=len(word)
    
print("\nYou inserted:")
print(f"- {i-1} words")
print(f"- {word_len} characters")
print("\nProgram ending.")