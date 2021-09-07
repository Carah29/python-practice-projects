#trying to check if its a valid email
#need to do a better verification
#mayb using regex

while True:
    email = input("Enter email: ")
    if email.find("@") == -1:
        continue
    else:
        break
email_slicer = email.split(sep="@")

username = email_slicer[0]
domain_name = email_slicer[1]

print(username, domain_name)
