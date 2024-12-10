import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# Error handling if user inputs a number
def generate_phonetic():
    user_word = input("What word would you like to convert?:  ").upper()
    try:
        name_letters = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(name_letters)


generate_phonetic()




