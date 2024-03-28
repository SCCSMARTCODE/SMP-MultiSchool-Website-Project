# from os import getenv, environ
#
# """This should be removed ASAP"""
# environ["DB_PASSWD"] = "smp_pass_master"
# environ["DB_HOST"] = "localhost"
# environ["DB_USER"] = "smp_master"
# environ["DB_NAME"] = "smp_base_db"
# environ["DB_TYPE"] = "db"
# """This should be removed ASAP"""
#
#
# print("emmanuel is coming".upper())

# from PIL import Image
#
#
# image = Image.open('C:/Users/USER/Desktop/nn.png')
#
# new_image = image.resize((1800, 1800))
#
# # new_image.save('C:/Users/USER/Desktop/nn1.png')
#
# import smtplib
# from email.message import EmailMessage
#
# msg = EmailMessage()
#
# msg['Subject'] = 'subject'
# msg['From'] = 'sccsmart247@gmail.com'
# msg['To'] = 'sccsmart247@gmail.com'
# msg.set_content('content')
# msg.add_alternative('message')
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 456) as smtp:
#     smtp.login('sccsmart247@gmail.com', 'jemw amml ymty cukm')
#     smtp.send_message(msg)


import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg['Subject'] = 'subject'
msg['From'] = 'sccsmart247@gmail.com'
msg['To'] = 'sccsmart247@gmail.com'
msg.set_content('content')
msg.add_alternative('message')

# Provide the hostname of the SMTP server, not the email address
smtp_server = 'smtp.gmail.com'
smtp_port = 465

with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
    smtp.login('sccsmart247@gmail.com', 'jemw amml ymty cukm')
    smtp.send_message(msg)
