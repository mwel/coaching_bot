""" Mailing feature. Sends a summary to the user upon completion of sign up."""

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from constants import MAIL_constant

# variables
smtp_address =      MAIL_constant.post_in_server
smtp_port =         MAIL_constant.port
sender_address =    MAIL_constant.mail_user_in
password =          MAIL_constant.MAIL_ACCOUNT_PW

# send summary email to user after completion of bot questions
def summary_mail(recipient_name, summary, recipient_address):

    # open connection to mail server and authenticate
    server = smtplib.SMTP_SSL(smtp_address, smtp_port)
    server.login(sender_address, password)

    # create multipart object, the email consists of
    message = MIMEMultipart()

    # defined from address, to address and subject of the email
    message['From'] = sender_address
    message['To'] = recipient_address

    subject = 'Coaching Bot | Confirmation - sign up complete'
    message['Subject'] = subject

    # email body
    body =   f"""Hi {recipient_name}, \t
        thanks for signing up. This is the confirmation for your sign up with the coaching program by wavehoover. \n 
        {summary}\n
        Looking forward to meeting you!\n
        Your wavehoover Team"""
    
    # create the text object for the email
    message.attach(MIMEText(body, 'plain'))


    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()


# if __name__ == '__main__':
#     summary_mail('Subject: Automated e-mail', 'my_test_email@test.com', 'Automated email from the coaching Bot by wavehoover.')