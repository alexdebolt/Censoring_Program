# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()



def sensor_text(email, text):
    split_email = email.split()
    censored_email_list = []
    for word in split_email:
        if text == word:
            word = "@#$%^&*"
            censored_email_list.append(word)
        if text != word:
            censored_email_list.append(word)
     
    censored_email = " ".join(censored_email_list)
    return censored_email


