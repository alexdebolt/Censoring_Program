# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def censor_simple(email, text_to_censor):

    censored = ""
    # this for loop censors the text regardless of if it is in the email, converts it to @ signs
    for i in range(0, len(text_to_censor)):
        if text_to_censor[i] == " ":
            censored += " "
        else:
            censored += "@"
    # if the text_to_censor is not in email, the email is unchanged
    return email.replace(text_to_censor, censored)

# print(sensor_simple(email_one, "Till next month,"))


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

# function to censor specific words given in a list
def specific_censor(email, list_to_censor):
    # iterate through each word in list and censor it
    for word in list_to_censor:
        censored_word = ""
        for i in range(0, len(word)):
            if word[i] == " ":
                censored_word += " "
            else:
                censored_word += "#"
        email = email.replace(word, censored_word)
    return email
       
# print(specific_censor(email_two, proprietary_terms))


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

# function to censor proprietary_terms and negative words if they appear more than once
def prop_and_negative_censor(email, prop_list, neg_list):
    # iterate through each word in list and censor it
    for word in prop_list:
        censored_word = ""
        for i in range(0, len(word)):
            if word[i] == " ":
                censored_word += " "
            else:
                censored_word += "#"
        email = email.replace(word, censored_word)

    # removing negative words if they appear twice
    for word in neg_list:
        censored_negative_word = ""
        if email.count(word) >= 2:
            for i in range(0, len(word)):
                if word[i] == " ":
                    censored_negative_word += " "
                else:
                    censored_negative_word += "@"
        email = email.replace(word, censored_negative_word)
    
    return email

# print(prop_and_negative_censor(email_three, proprietary_terms, negative_words))

# made a short function to check number of times each negative word appeared in email three, results: none appeared more than once
def find_negative_words(neg_words, email):
    for word in neg_words:
        if word in email:
            print("{word} is in email {times} time(s)!".format(word=word, times=email.count(word)))

# find_negative_words(negative_words, email_three)