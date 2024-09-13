#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt", mode="r") as name_file:
    name_list = name_file.readlines()

for names in name_list:
    with open(f"Input/Letters/starting_letter.txt", mode="r") as file:
        contents = file.readlines()
        clean_contents = contents[0]

    with open(f"Output/ReadyToSend/{names.strip("\n")}.txt", mode="w") as file:
        new_contents = clean_contents.replace("[name]", f"{names.strip("\n")}")
        file.write(f"{new_contents}")
        for lines in range(1,7):
            file.write(contents[lines])

# Another way to do it
# PLACEHOLDER = "[name]"
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.docx") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.dox", mode="w") as completed_letter:
#             completed_letter.write(new_letter)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp