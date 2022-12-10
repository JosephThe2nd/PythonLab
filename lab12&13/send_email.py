from email.message import EmailMessage
import ssl #pentru securitate
import smtplib
import re #for Regular Expressions
import sys #for stopping the program quit() / exit()


email_sender = "opdeadly3@gmail.com"
email_password = "pbgxmarkezbdgurd"
email_receiver = "mmfgfkxmbrycmzslxe@tmmbt.com" #https://10minutemail.com/


pattern = re.compile("^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$") #the pattern of an email(?- un singur caracter allowed, \w alfa numerical caracters)
if re.search(pattern,email_receiver):
    print(f"{email_receiver} is a valid email")
else: 
    sys.exit(f"{email_receiver} is not a valid email")
    



subject = "This is a test Subject"
body = """
This is a test email
Don't mind this email
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("The email has been sent successfully")
