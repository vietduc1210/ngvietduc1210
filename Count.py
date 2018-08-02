sentence = input("Enter the sentence :")
sentence = sentence.lower().replace(" " ,"")

letter_counts = {}
for letter in sentence:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

for letter, number in sorted(letter_counts.items()):
    print(letter, number)