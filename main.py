# i
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = "saradpractices@gmail.com", password = "s5J4y4(TA%X#5%Vo")
#     connection.sendmail(from_addr= "saradpractices@gmail.com", to_addrs="sarad2122@gmail.com", msg = "Subject:Testing the program\n\nHello Its from Python")
#
#

import smtplib
import datetime as dt
import random
import tkinter
import pandas

def get_quote():
    """
    Randomly selects a quote from quotes in motivation.txt file
    :return: A pair in format (Author,Quote)
    """
    filereader = open("quotes.txt","r")
    data = filereader.read()
    quotes = data.split("\n")
    quote = random.choice(quotes)
    return (quote.split('-')[1],quote.split('-')[0])


def get_emails():
    """
    Reads and sends all emails in motivation.txt file.
    :return: a list with all emails in the file
    """
    with open("motivation.txt", "r") as maillist:
        emails = maillist.read().split("\n")
        return emails

def send_quote():
    """
    Gets a quote, then sends to everyone in the list
    :return:
    """
    quote = get_quote()
    emails = get_emails()
    for email in emails:
        send(email,"Motivation Today from "+ quote[0],quote[1])



def send(email, title,body):
    """
    Sends the given body with given text to given email.
    :param email: Email address
    :param title: Title of email to be sent
    :param body: Message body of email
    :return:
    """
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = "saradpractices@gmail.com", password = "Maybe I will put my password next time :p")
        try:
            connection.sendmail(from_addr="saradpractices@gmail.com", to_addrs=email,msg = f"Subject:{title}\n\n{body}")
        except:
            print(f"Couldnt send email to {email}")

def send_message(individual):
    """
    Selects a random tempate, extracts info of people and sends them a Happy Birthday Message
    :param individual: a dataframe with people orn on todays date
    :return:
    """
    file_num = str(random.choice([1,2,3]))
    file = "D:\Python\Birthday\letter_templates/letter_"+file_num+".txt"
    file_text = ""
    with open(file,"r") as f:
        file_text = f.read()
    people = individual.values
    for person in people:
        body = file_text.replace("[NAME]",person[0])
        title = "Happy Birthday"
        email = person[1]
        send(email, title, body)


def send_birthday_wish():
    """

    :return:
    """
    data = pandas.read_csv("birthdays.csv")
    today = dt.datetime.now()
    individual = data.loc[(data["month"] == today.month) & (data["day"] == today.day)]
    send_message(individual)



#####################################   BASIC UI SETUP    ##################
window = tkinter.Tk()
window.title("Motivational quote or Birthday wish")
window.minsize(width=200,height = 200)

motivate_button = tkinter.Button(text = "Send Motivational Quotes",command = send_quote,width = 20, pady = 20)
motivate_button.pack()
birthday_button = tkinter.Button(text = "Birthday Wish",command = send_birthday_wish,width = 20, pady = 20)
birthday_button.pack()






window.mainloop()

