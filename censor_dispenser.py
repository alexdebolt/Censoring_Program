# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def sensor_simple(email, text_to_censor):
    censored = ""
    # this for loop censors the text regardless of if it is in the email, converts it to @ signs
    for i in range(0, len(text_to_censor)):
        if text_to_censor[i] == " ":
            censored += " "
        else:
            censored += "@"
    # if the text_to_censor is not in email, the email is unchanged
    return email.replace(text_to_censor, censored)

print(sensor_simple(email_one, "Till next month,"))

