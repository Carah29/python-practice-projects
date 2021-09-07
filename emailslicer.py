email = input("Enter email: ")
email_slicer = email.split(sep="@")

username = email_slicer[0]

#domain name
domain_name = email_slicer[1]
print(username, domain_name)
