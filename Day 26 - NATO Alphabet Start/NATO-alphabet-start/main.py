import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
user_word = input("What word would you like to convert?:  ").upper()
name_letters = [phonetic_dict[letter] for letter in user_word]
print(name_letters)


