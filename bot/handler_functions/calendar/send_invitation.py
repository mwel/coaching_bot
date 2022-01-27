""" Mailing a calendar invite."""

# imports
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
def send_invitation(recipient_name, summary, recipient_address, ics):

    # open connection to mail server and authenticate
    server = smtplib.SMTP_SSL(smtp_address, smtp_port)
    server.login(sender_address, password)

    # create multipart object, the email consists of
    message = MIMEMultipart()

    # defined from address, to address and subject of the email
    message['From'] = sender_address
    message['To'] = recipient_address

    subject = 'Coaching Bot | First Session Invite'
    message['Subject'] = subject

    # email body
    body =   f"""Hi {recipient_name}, \t
        this is the invitation for your first 1:1 coaching session. \n 
        {summary}\n
        Looking forward to meeting you!\n
        Your wavehoover Team"""
    
    # create the text object for the email
    message.attach(MIMEText(body, 'plain'))


    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()


# if __name__ == '__main__':
#     confirmation_mail('Subject: Automated e-mail', 'my_test_email@test.com', 'Automated email from the coaching Bot by wavehoover.')