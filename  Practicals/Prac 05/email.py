
def main():
    """dictionary of emails to names"""
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        user_name = get_from_email(user_email)
        confirmation = input ("Is your name {}? (Y/N})".format(user_name))
        if confirmation.upper() != "Y" and confirmation != "":
            user_name = input("Name: ")
        email_to_name[user_email] = user_name
        user_email = input("Email: ")
    for user_email, name in email_to_name.items():
        print("{} ({})".format(name, user_email))

def get_from_email(user_email):
    """Extract expected name from email"""
    fullname = user_email.spilt('@')[0]
    user_name = fullname.spilt('.')
    name = " ".join(user_name).title()
    return name





main()
