import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "enter_your_email_here@gmail.com"
MY_PASSWORD = "enter_your_security_code here"
# Creating a tuple of what the current month and day are
Now = dt.datetime.now()
current_day = (Now.month,Now.day)

# Opening up the birthdays.csv file and using dictionary comprehension to create a new dictionary
# Template for this is: new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if current day matches any birthdays in the csv file, replace [NAME], send email
if current_day in birthdays_dict:
    birthday_person = birthdays_dict[current_day]
    letter_choice = random.randint(1,3)
    if letter_choice == 1:
        with open("letter_templates/letter_1.txt") as file:
            message = file.read()
            new_message = message.replace("[NAME]", birthday_person["name"])
    if letter_choice == 2:
        with open("letter_templates/letter_2.txt") as file:
            message = file.read()
            new_message = message.replace("[NAME]", birthday_person["name"])
    if letter_choice == 3:
        with open("letter_templates/letter_3.txt") as file:
            message = file.read()
            new_message = message.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject:Happy Birthday!\n\n{new_message}")




