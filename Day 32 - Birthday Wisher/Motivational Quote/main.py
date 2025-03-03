# # password ="Llama123"

import smtplib
import datetime as dt
import random
# ------------------------------------File Management Section------------------------------------------------
def get_quote():
    with open("quotes.txt", mode="r") as file:
        lines = file.readlines()
        quote = random.choice(lines)
        print("quote")
        return quote

# ------------------------------------Email Section----------------------------------------------------------
def send_email():
    my_email = "pythonlearning795@gmail.com"
    password = "zpwj glkr zlyl twkb"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="pythonlearning795@yahoo.com",
                            msg=f"Subject:Motivational Quote\n\n{get_quote()}"
                            )
        print("Email")

# ------------------------------------Datetime Section-------------------------------------------------------
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 3:
    send_email()


